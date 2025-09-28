import os
import sys
import json
import types
import importlib
from unittest.mock import patch


# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# Prepare lightweight fake modules to satisfy imports inside _gemini_proxy
# We'll temporarily inject these into sys.modules while importing the module

# Save any originals so we can restore them after import
_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'firebase_admin',
    'firebase_admin.firestore',
    'utils',
    'auth',
    'google',
    'google.genai',
    'google.genai.types',
]
for name in _names_to_fake:
    _orig_sys_modules[name] = sys.modules.get(name)

# Fake firebase_functions.https_fn.Response to capture returned data
firebase_functions = types.ModuleType('firebase_functions')

class FakeResponse:
    def __init__(self, response=None, mimetype=None, status=200, **kwargs):
        # Mirror the small subset of the interface tests expect
        self.status_code = status
        if isinstance(response, (dict, list)):
            self._body_text = json.dumps(response)
        else:
            self._body_text = '' if response is None else response
        self.headers = kwargs.get('headers', {})

    def get_data(self, as_text=False):
        if as_text:
            return self._body_text
        return self._body_text.encode('utf-8')

firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
sys.modules['firebase_functions'] = firebase_functions

# Fake firebase_admin and its firestore submodule to satisfy optional imports in the proxy
firebase_admin = types.ModuleType('firebase_admin')
firestore_mod = types.ModuleType('firebase_admin.firestore')

# Minimal Client type for annotations and a no-op client() factory
class _DummyClient:  # pragma: no cover - just a stub for import-time type hints
    pass

def _dummy_client():
    # Return a simple object; logic using it is patched in tests
    return types.SimpleNamespace()

# Decorator stub used by perform_atomic_debit; never actually invoked in tests
def _transactional(fn=None):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

# Populate stubs on the firestore module
setattr(firestore_mod, 'Client', _DummyClient)
setattr(firestore_mod, 'client', _dummy_client)
setattr(firestore_mod, 'transactional', _transactional)
setattr(firestore_mod, 'SERVER_TIMESTAMP', object())

# Attach firestore submodule to firebase_admin package and register in sys.modules
setattr(firebase_admin, 'firestore', firestore_mod)
sys.modules['firebase_admin'] = firebase_admin
sys.modules['firebase_admin.firestore'] = firestore_mod

# Fake utils module (provides functions imported by _gemini_proxy)
utils_mod = types.ModuleType('utils')


def _fake_create_json_response(success: bool, payload: any, status_code: int):
    response_body = {"success": success, "payload": payload}
    return firebase_functions.https_fn.Response(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})


def _fake_get_api_key(llm_family=None):
    return 'DUMMY_GEMINI_KEY'


def _fake_verify_firebase_token(req):
    # Default: no-op (successful)
    return {}


utils_mod.create_json_response = _fake_create_json_response
utils_mod.get_api_key = _fake_get_api_key
utils_mod.verify_firebase_token = _fake_verify_firebase_token
sys.modules['utils'] = utils_mod

# Fake auth module with validate_auth_key
auth_mod = types.ModuleType('auth')


def _fake_validate_auth_key(val: str) -> bool:
    return True


auth_mod.validate_auth_key = _fake_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake google.genai and types modules
google_mod = types.ModuleType('google')
genai_mod = types.ModuleType('google.genai')
types_mod = types.ModuleType('google.genai.types')

class DummyGenerateContentConfig:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

class DummyContent:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

types_mod.GenerateContentConfig = DummyGenerateContentConfig
types_mod.Content = DummyContent

# Provide a dummy Client implementation; tests will patch this when needed
class DummyClient:
    def __init__(self, api_key):
        self.api_key = api_key
        class Models:
            def generate_content(self, **params):
                raise NotImplementedError("generate_content not implemented for dummy client")
        self.models = Models()

genai_mod.Client = DummyClient
# Also expose types on genai module (in case of attribute access)
genai_mod.types = types_mod

google_mod.genai = genai_mod
sys.modules['google'] = google_mod
sys.modules['google.genai'] = genai_mod
sys.modules['google.genai.types'] = types_mod

# Import the module under test after preparing the fake imports
# Resolve the actual repository 'functions' directory (tests files live under tests/, so climb up to repo root)
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_gemini_proxy.py')
spec = importlib.util.spec_from_file_location('api_v1_00._gemini_proxy', module_path)
_gemini = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_gemini)

# Restore original sys.modules mappings to avoid side-effects for other tests
for name, orig in _orig_sys_modules.items():
    if orig is None:
        try:
            del sys.modules[name]
        except KeyError:
            pass
    else:
        sys.modules[name] = orig

# Helper request stub used in tests
class DummyRequest:
    def __init__(self, headers=None, method='POST', json_data=None, raise_on_get_json=False):
        self.headers = headers or {}
        self.method = method
        self._json_data = json_data
        self._raise = raise_on_get_json

    def get_json(self, silent=False):
        if self._raise:
            raise Exception('Malformed JSON')
        return self._json_data


def _parse_response(resp):
    data = resp.get_data(as_text=True)
    return json.loads(data)


# -----------------------------
# Tests
# -----------------------------


def test_verify_firebase_token_failure_returns_401():
    req = DummyRequest(headers={_gemini.AUTH_HEADER_NAME: 'ok'}, method='POST')
    with patch.object(_gemini, 'verify_firebase_token', side_effect=Exception('invalid token')):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Unauthorized' in payload['payload']


def test_missing_auth_header_returns_401():
    # no app auth header
    req = DummyRequest(headers={}, method='POST', json_data={'model': 'm', 'contents': 'c', 'config': {}})
    with patch.object(_gemini, 'validate_auth_key', return_value=True), patch.object(_gemini, 'verify_firebase_token', return_value={}):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['payload']


def test_invalid_auth_key_returns_403():
    headers = {_gemini.AUTH_HEADER_NAME: 'bad'}
    req = DummyRequest(headers=headers, method='POST', json_data={'model': 'm', 'contents': 'c', 'config': {}})
    with patch.object(_gemini, 'validate_auth_key', return_value=False), patch.object(_gemini, 'verify_firebase_token', return_value={}):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['payload']


def test_non_post_method_returns_405():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='GET')
    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 405
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'POST method required' in payload['payload']


def test_malformed_json_returns_400():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', raise_on_get_json=True)
    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid JSON payload' in payload['payload']


def test_rehydrate_params_error_returns_400():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    # missing 'model' to cause KeyError inside rehydrate_params
    req = DummyRequest(headers=headers, method='POST', json_data={'contents': 'x', 'config': {}})
    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Error hydrating params' in payload['payload']


def test_get_api_key_failure_returns_500():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'model': 'g', 'contents': 'hi', 'config': {}})
    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_gemini, 'get_api_key', side_effect=Exception('boom')):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Could not retrieve API key' in payload['payload']


def test_successful_flow_calls_genai_and_returns_payload():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'model': 'gem-model', 'contents': 'hello', 'config': {}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient:
        def __init__(self, api_key):
            self.api_key = api_key
            self.models = self

        def generate_content(self, **params):
            class FakeResp:
                def __init__(self):
                    # include usage metadata expected by get_usage()
                    self.usage_metadata = types.SimpleNamespace(prompt_token_count=1, total_token_count=2)

                def to_json_dict(self_inner):
                    return { 'result': 'ok', 'received_model': params.get('model') }
            return FakeResp()

    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_gemini, 'bill_with_retry', return_value=("ok", 99.5)), \
         patch.object(_gemini, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_gemini.genai, 'Client', FakeClient):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert isinstance(payload['payload'], dict)
    assert payload['payload']['result'] == 'ok'
    assert payload['payload']['received_model'] == 'gem-model'


def test_genai_exception_with_status_code_is_returned_as_error_status():
    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'model': 'g', 'contents': 'hey', 'config': {}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class CustomErr(Exception):
        pass

    err = CustomErr('rate limited')
    err.status_code = 502

    class ErrClient:
        def __init__(self, api_key):
            self.api_key = api_key
            self.models = self

        def generate_content(self, **params):
            raise err

    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_gemini, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_gemini.genai, 'Client', ErrClient):
        resp = _gemini._gemini_proxy(req)

    assert resp.status_code == 502
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Internal Server Error' in payload['payload']
