import os
import sys
import json
import types
import importlib
from unittest.mock import patch


# Ensure the functions/ directory is importable as a top-level module location
# Project root is three levels up from this test file (tests/functions/api_v1_00/...)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# Prepare lightweight fake modules to satisfy imports inside _openai_proxy
# We'll temporarily inject these into sys.modules while importing the module

# Save any originals so we can restore them after import
_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'utils',
    'auth',
    'openai',
    'firebase_admin',
    'billing',
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

# Fake utils module (provides functions imported by _openai_proxy)
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
    def __init__(self, api_key=None, timeout=None):
        self.api_key = api_key
        self.timeout = timeout
        # The proxy expects openai_client.responses.create / parse
        self.responses = self

    def create(self, **params):
        raise NotImplementedError("create not implemented for dummy client")

    def parse(self, **params):
        raise NotImplementedError("parse not implemented for dummy client")


openai_mod.OpenAI = DummyOpenAI
openai_mod.APIError = APIError
sys.modules['openai'] = openai_mod

# Fake billing module to satisfy imports in v1_00 _openai_proxy (billing helpers)
billing_mod = types.ModuleType('billing')

def _fake_ensure_balance_positive(db, user_id):
    return (True, 100.0)

def _fake_calculate_cost(model_id, input_tokens, output_tokens):
    return 0.0

def _fake_bill_with_retry(db, user_id, model_id, usage, cost, reason='usage'):
    return ("ok", 100.0)

billing_mod.ensure_balance_positive = _fake_ensure_balance_positive
billing_mod.calculate_cost = _fake_calculate_cost
billing_mod.bill_with_retry = _fake_bill_with_retry
sys.modules['billing'] = billing_mod

# Fake firebase_admin module providing a minimal firestore.client to avoid
# attempting to initialize the real Firebase SDK during tests
firebase_admin_mod = types.ModuleType('firebase_admin')
firebase_admin_mod.firestore = types.SimpleNamespace(client=lambda: types.SimpleNamespace(), Client=type('Client', (), {}))
sys.modules['firebase_admin'] = firebase_admin_mod

# Import the module under test after preparing the fake imports
# Use a package-qualified import to ensure we always import the v1_00 implementation
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_openai_proxy.py')
spec = importlib.util.spec_from_file_location('api_v1_00._openai_proxy', module_path)
_openai = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_openai)


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
    req = DummyRequest(headers={_openai.AUTH_HEADER_NAME: 'ok'}, method='POST')
    with patch.object(_openai, 'verify_firebase_token', side_effect=Exception('invalid token')):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Unauthorized' in payload['payload']


def test_missing_auth_header_returns_401():
    # no app auth header
    req = DummyRequest(headers={}, method='POST', json_data={'call_type': 'create', 'call_params': {}})
    with patch.object(_openai, 'validate_auth_key', return_value=True), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['payload']


def test_invalid_auth_key_returns_403():
    headers = {_openai.AUTH_HEADER_NAME: 'bad'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'create', 'call_params': {}})
    with patch.object(_openai, 'validate_auth_key', return_value=False), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['payload']


def test_non_post_method_returns_405():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='GET')
    with patch.object(_openai, 'validate_auth_key', return_value=True), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 405
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'POST method required' in payload['payload']


def test_malformed_json_returns_400():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', raise_on_get_json=True)
    with patch.object(_openai, 'validate_auth_key', return_value=True), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid JSON payload' in payload['payload']


def test_missing_or_invalid_call_type_or_call_params_returns_400():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': None, 'call_params': {}})
    with patch.object(_openai, 'validate_auth_key', return_value=True), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing or invalid required fields' in payload['payload']


def test_invalid_call_type_returns_400():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'bad', 'call_params': {}})
    with patch.object(_openai, 'validate_auth_key', return_value=True), patch.object(_openai, 'verify_firebase_token', return_value={}):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Invalid 'call_type'" in payload['payload']


def test_get_api_key_failure_returns_500():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'create', 'call_params': {'model': 'm', 'input': 'hi'}})
    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', side_effect=Exception('boom')):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Could not retrieve API key' in payload['payload']


def test_parse_missing_input_or_text_format_returns_400():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    # missing 'text_format' to trigger the parse validation
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'parse', 'call_params': {'model': 'm', 'input': 'hi'}})

    class NoopOpenAI:
        def __init__(self, api_key=None, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self

        def parse(self, **p):
            return None

        def create(self, **p):
            return None

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='KEY'), \
         patch.object(_openai.openai, 'OpenAI', NoopOpenAI):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Missing 'input' or 'text_format' for parse call" in payload['payload']


def test_create_missing_input_returns_400():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'call_type': 'create', 'call_params': {'model': 'm'}})

    class NoopOpenAI:
        def __init__(self, api_key=None, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self

        def parse(self, **p):
            return None

        def create(self, **p):
            return None

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='KEY'), \
         patch.object(_openai.openai, 'OpenAI', NoopOpenAI):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Missing 'input' for create call" in payload['payload']


def test_successful_create_calls_openai_and_returns_payload():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'call_type': 'create', 'call_params': {'model': 'gem-model', 'input': 'hello'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient:
        def __init__(self, api_key, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self

        def create(self, **params):
            class FakeResp:
                def model_dump(self_inner, mode='json'):
                    return {'result': 'ok', 'received_model': params.get('model'), 'usage': {'input_tokens': 1, 'output_tokens': 2}}
            return FakeResp()

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='OPENAI-KEY'), \
         patch.object(_openai, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_openai, 'bill_with_retry', return_value=("ok", 95.0)), \
         patch.object(_openai.firestore, 'client', return_value=types.SimpleNamespace()), \
         patch.object(_openai.openai, 'OpenAI', FakeClient):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert isinstance(payload['payload'], dict)
    assert payload['payload']['result'] == 'ok'
    assert payload['payload']['received_model'] == 'gem-model'


def test_successful_parse_calls_openai_and_returns_parsed_and_usage():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'call_type': 'parse', 'call_params': {'model': 'gem-model', 'input': 'hello', 'text_format': 'FileSummaryModel'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient2:
        def __init__(self, api_key, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self

        def parse(self, **params):
            class FakeOutputParsed:
                def __init__(self, data):
                    self._data = data

                def dict(self):
                    return self._data

            class FakeResp:
                def __init__(self, data, usage):
                    self.output_parsed = FakeOutputParsed(data)
                    self._usage = usage

                def model_dump(self_inner, mode='json'):
                    return {'usage': self_inner._usage}

            # detect whether text_format was left as a string
            is_text_format_string = isinstance(params.get('text_format'), str)
            parsed = {'result': 'ok', 'received_model': params.get('model'), 'is_text_format_string': is_text_format_string}
            usage = {'input_tokens': 1, 'output_tokens': 2, 'prompt_tokens': 5}
            return FakeResp(parsed, usage)

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='OPENAI-KEY'), \
         patch.object(_openai, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_openai, 'bill_with_retry', return_value=("ok", 95.0)), \
         patch.object(_openai.firestore, 'client', return_value=types.SimpleNamespace()), \
         patch.object(_openai.openai, 'OpenAI', FakeClient2):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert payload['payload']['output_parsed']['result'] == 'ok'
    assert payload['payload']['output_parsed']['received_model'] == 'gem-model'
    # The proxy should have replaced the text_format string with the model (i.e., not a string)
    assert payload['payload']['output_parsed']['is_text_format_string'] is False
    assert payload['payload']['usage']['prompt_tokens'] == 5


def test_openai_api_error_with_status_code_is_returned_as_error_status():
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'call_type': 'create', 'call_params': {'model': 'g', 'input': 'hey'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Use the module's openai.APIError so the proxy's except block catches it
    err = _openai.openai.APIError('rate limited')
    err.status_code = 502

    class ErrClient:
        def __init__(self, api_key=None, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self

        def create(self, **params):
            raise err

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='OPENAI-KEY'), \
         patch.object(_openai, 'ensure_balance_positive', return_value=(True, 100.0)), \
         patch.object(_openai.firestore, 'client', return_value=types.SimpleNamespace()), \
         patch.object(_openai.openai, 'OpenAI', ErrClient):
        resp = _openai._openai_proxy(req)

    assert resp.status_code == 502
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'OpenAI API Error' in payload['payload']
