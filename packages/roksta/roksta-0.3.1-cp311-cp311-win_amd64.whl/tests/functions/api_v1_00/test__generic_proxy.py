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

# Prepare lightweight fake modules to satisfy imports inside _generic_proxy
# We'll temporarily inject these into sys.modules while importing the module

# Save any originals so we can restore them after import
_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'utils',
    'auth',
    'openai',
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

# Fake utils module (provides functions imported by _generic_proxy)
utils_mod = types.ModuleType('utils')


def _fake_create_json_response(success: bool, payload: any, status_code: int):
    response_body = {"success": success, "payload": payload}
    return firebase_functions.https_fn.Response(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})


def _fake_get_api_key(llm_family=None):
    return 'DUMMY_KEY'


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

# Fake openai module with APIError and a default OpenAI class
openai_mod = types.ModuleType('openai')

class APIError(Exception):
    pass


class DummyOpenAI:
    def __init__(self, base_url=None, api_key=None, timeout=None):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        class Completions:
            def create(self, **params):
                raise NotImplementedError("create not implemented for dummy client")
            def parse(self, **params):
                raise NotImplementedError("parse not implemented for dummy client")
        class Chat:
            def __init__(self):
                self.completions = Completions()
        self.chat = Chat()

openai_mod.OpenAI = DummyOpenAI
openai_mod.APIError = APIError
sys.modules['openai'] = openai_mod

# Import the module under test after preparing the fake imports
#_generic = importlib.import_module('_generic_proxy')

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_generic_proxy.py')
spec = importlib.util.spec_from_file_location('api_v1_00._generic_proxy', module_path)
_generic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_generic)

# Patch Firestore client and billing functions to avoid external dependencies during tests
# Provide a dummy Firestore client and make balance checks/billing no-ops.
_generic.firestore = types.SimpleNamespace(client=lambda: object())

def _fake_ensure_balance_positive(db, user_id):
    return True, 100.0

def _fake_extract_usage(llm_family=None, call_type=None, model_id=None, request_payload=None, response_payload=None):
    # Default to zero-usage unless present in the payload
    usage = response_payload.get('usage', {}) if isinstance(response_payload, dict) else {}
    in_tokens = usage.get('prompt_tokens', 0) or usage.get('input_tokens', 0) or 0
    out_tokens = usage.get('completion_tokens', 0) or usage.get('output_tokens', 0) or 0
    return {"input_tokens": in_tokens, "output_tokens": out_tokens}

def _fake_calculate_cost(model_id=None, input_tokens=0, output_tokens=0):
    return 0.0

def _fake_bill_with_retry(db=None, user_id=None, model_id=None, usage=None, cost=None, reason=None):
    return "ok", 100.0

_generic.ensure_balance_positive = _fake_ensure_balance_positive
_generic.extract_usage = _fake_extract_usage
# Compatibility shim: some versions of the module call get_usage(response) instead of extract_usage(...)
_generic.get_usage = lambda response: _fake_extract_usage(response_payload=response)
_generic.calculate_cost = _fake_calculate_cost
_generic.bill_with_retry = _fake_bill_with_retry

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
    req = DummyRequest(headers={_generic.AUTH_HEADER_NAME: 'ok'}, method='POST')
    with patch.object(_generic, 'verify_firebase_token', side_effect=Exception('invalid token')):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Unauthorized' in payload['payload']


def test_missing_auth_header_returns_401():
    req = DummyRequest(headers={}, method='POST', json_data={'llm_family': 'openai', 'call_type': 'create', 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['payload']


def test_invalid_auth_key_returns_403():
    headers = {_generic.AUTH_HEADER_NAME: 'bad'}
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'openai', 'call_type': 'create', 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=False), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['payload']


def test_non_post_method_returns_405():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='GET')
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 405
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'POST method required' in payload['payload']


def test_malformed_json_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', raise_on_get_json=True)
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid JSON payload' in payload['payload']


def test_missing_llm_family_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'create', 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Missing 'llm_family'" in payload['payload']


def test_invalid_llm_family_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'notreal', 'call_type': 'create', 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid LLM family' in payload['payload']


def test_missing_or_invalid_call_type_or_call_params_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    # Use an empty dict for call_params so the proxy can safely access call_params.get()
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'openai', 'call_type': None, 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing or invalid required fields' in payload['payload']


def test_invalid_call_type_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'openai', 'call_type': 'bad', 'call_params': {}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), patch.object(_generic, 'verify_firebase_token', return_value={}):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Invalid 'call_type'" in payload['payload']


def test_get_api_key_failure_returns_500():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'openai', 'call_type': 'create', 'call_params': {'model': 'm'}})
    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', side_effect=Exception('boom')):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Could not retrieve API key' in payload['payload']


def test_parse_without_response_format_returns_400():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'llm_family': 'openai', 'call_type': 'parse', 'call_params': {'model': 'm'}})

    class NoopOpenAI:
        def __init__(self, api_key=None, base_url=None, timeout=None):
            class Completions:
                def create(self, **p):
                    return None
                def parse(self, **p):
                    return None
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()

    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', return_value='KEY'), \
         patch.object(_generic.openai, 'OpenAI', NoopOpenAI):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Missing 'response_format' for parse call" in payload['payload']


def test_successful_create_calls_openai_and_returns_payload():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'llm_family': 'openai', 'call_type': 'create', 'call_params': {'model': 'gem-model', 'input': 'hello'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient:
        def __init__(self, api_key, base_url=None, timeout=None):
            self.api_key = api_key
            class Completions:
                def create(self_inner, **params):
                    class FakeResp:
                        def model_dump(self_inner, mode='json'):
                            return {'result': 'ok', 'received_model': params.get('model')}
                    return FakeResp()
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()

    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_generic.openai, 'OpenAI', FakeClient):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert isinstance(payload['payload'], dict)
    assert payload['payload']['result'] == 'ok'
    assert payload['payload']['received_model'] == 'gem-model'


def test_openai_api_error_with_status_code_is_returned_as_error_status():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'llm_family': 'openai', 'call_type': 'create', 'call_params': {'model': 'g', 'input': 'hey'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Use the module's openai.APIError so the proxy's except block catches it
    err = _generic.openai.APIError('rate limited')
    err.status_code = 502

    class ErrClient:
        def __init__(self, api_key=None, base_url=None, timeout=None):
            class Completions:
                def create(self_inner, **params):
                    raise err
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()

    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_generic.openai, 'OpenAI', ErrClient):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 502
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'OpenAI API Error' in payload['payload']


def test_parse_replaces_response_format_name_with_model_and_calls_openai():
    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'llm_family': 'openai', 'call_type': 'parse', 'call_params': {'model': 'gem-model', 'input': 'hello', 'response_format': 'FileSummaryModel'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient2:
        def __init__(self, api_key, base_url=None, timeout=None):
            class Completions:
                def parse(self_inner, **params):
                    class FakeResp:
                        def model_dump(self_inner, mode='json'):
                            return {
                                'result': 'ok',
                                'received_model': params.get('model'),
                                'is_response_format_string': isinstance(params.get('response_format'), str)
                            }
                    return FakeResp()
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()

    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_generic.openai, 'OpenAI', FakeClient2):
        resp = _generic._generic_proxy(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert payload['payload']['result'] == 'ok'
    # The proxy should have replaced the response_format string with the model (i.e., not a string)
    assert payload['payload']['is_response_format_string'] is False
