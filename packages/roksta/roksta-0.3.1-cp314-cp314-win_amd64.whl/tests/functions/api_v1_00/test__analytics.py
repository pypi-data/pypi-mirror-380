import os
import sys
import json
import types
import importlib
from unittest.mock import patch, Mock


# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# -----------------------------
# Provide lightweight fake modules to satisfy imports inside _analytics
# These are minimal and will be patched in individual tests as needed.
# -----------------------------
# Save any originals so we can restore them after import
_orig_sys_modules = {}
_names_to_fake = ['firebase_functions', 'utils', 'auth', 'httpx']
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

# Fake utils module (avoid google.cloud import at module import time)
utils_mod = types.ModuleType('utils')

def _dummy_get_secret_key(name: str) -> str:
    return 'DUMMY_SECRET'

# create_json_response should return a firebase_functions.https_fn.Response-like object
# with a JSON body containing at least 'success' and 'message' keys, and an HTTP status code.
def _dummy_create_json_response(success: bool, payload, status_code: int = 200, headers: dict | None = None):
    body = {'success': success, 'message': payload}
    return firebase_functions.https_fn.Response(response=body, status=status_code, headers=headers or {})

utils_mod.get_secret_key = _dummy_get_secret_key
utils_mod.create_json_response = _dummy_create_json_response
sys.modules['utils'] = utils_mod

# Fake auth module (validate_auth_key will be patched per-test as needed)
auth_mod = types.ModuleType('auth')

def _simple_validate_auth_key(val: str) -> bool:
    return bool(val)

auth_mod.validate_auth_key = _simple_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake httpx module to avoid external dependency; tests will patch Client behavior
httpx_mod = types.ModuleType('httpx')

class Request:
    def __init__(self, method, url, headers=None, content=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.content = content

class _DummyResponse:
    def __init__(self, status_code=200, text='', json_data=None, request=None, headers=None):
        self.status_code = status_code
        self.text = text if text is not None else ''
        self._json = json_data
        self.request = request
        self.headers = headers or {}
        # Provide a reason_phrase attribute similar to real httpx.Response
        self.reason_phrase = self.text or ''

    def json(self):
        # Prefer explicit JSON payload if provided, otherwise try to parse text
        if self._json is not None:
            return self._json
        try:
            return json.loads(self.text) if self.text else {}
        except Exception:
            return {}

    def raise_for_status(self):
        if 400 <= self.status_code:
            raise httpx_mod.HTTPStatusError(response=self)

class _DummyHttpxClient:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def post(self, url, json=None, timeout=30):
        resp = _DummyResponse(status_code=200, text='', json_data=None)
        resp.raise_for_status = Mock(return_value=None)
        resp.json = Mock(return_value={})
        return resp

class _DummyAsyncClient:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def get(self, url, headers=None, timeout=None):
        resp = _DummyResponse(status_code=200, text='', json_data=None)
        resp.raise_for_status = Mock(return_value=None)
        resp.json = Mock(return_value={})
        return resp

    async def post(self, url, json=None, data=None, headers=None, timeout=None):
        resp = _DummyResponse(status_code=200, text='', json_data=None)
        resp.raise_for_status = Mock(return_value=None)
        resp.json = Mock(return_value={})
        return resp

httpx_mod.Client = _DummyHttpxClient
httpx_mod.AsyncClient = _DummyAsyncClient
httpx_mod.Response = _DummyResponse
httpx_mod.Request = Request
httpx_mod.Headers = dict

class _HTTPStatusError(Exception):
    def __init__(self, *args, request=None, response=None):
        # Support both signatures:
        #   HTTPStatusError(response)
        #   HTTPStatusError(message, request=..., response=...)
        message = ""
        if response is None and len(args) == 1 and not isinstance(args[0], str):
            # Single positional non-string arg -> treated as response
            response = args[0]
        elif len(args) >= 1 and isinstance(args[0], str):
            message = args[0]
        elif len(args) > 1:
            message = args[0]
        super().__init__(message)
        self.request = request
        self.response = response

    def __str__(self):
        try:
            return f"{self.args[0]} (status={getattr(self.response,'status_code',None)})"
        except Exception:
            return self.args[0] if self.args else "HTTPStatusError"

class _RequestError(Exception):
    def __init__(self, message="", request=None):
        super().__init__(message)
        self.request = request

httpx_mod.HTTPStatusError = _HTTPStatusError
httpx_mod.RequestError = _RequestError
sys.modules['httpx'] = httpx_mod

# -----------------------------
# Import the module under test after preparing the fake imports
# -----------------------------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_analytics.py')
spec = importlib.util.spec_from_file_location('api_v1_00._analytics', module_path)
_analytics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_analytics)

# Restore original sys.modules mappings to avoid side-effects for other tests
for name, orig in _orig_sys_modules.items():
    if orig is None:
        try:
            del sys.modules[name]
        except KeyError:
            pass
    else:
        sys.modules[name] = orig

# Simple helper request stub used in the tests
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

def test_missing_auth_header_returns_401():
    req = DummyRequest(headers={}, method='POST')
    resp = _analytics._analytics(req)
    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing authentication key' in payload['message']


def test_invalid_auth_key_returns_403():
    headers = {_analytics.AUTH_HEADER_NAME: 'bad-token'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_analytics, 'validate_auth_key', return_value=False):
        resp = _analytics._analytics(req)
    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid authentication key' in payload['message']


def test_non_post_method_returns_405():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='GET')
    with patch.object(_analytics, 'validate_auth_key', return_value=True):
        resp = _analytics._analytics(req)
    assert resp.status_code == 405
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'POST method required' in payload['message']


def test_malformed_json_returns_400():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', raise_on_get_json=True)
    with patch.object(_analytics, 'validate_auth_key', return_value=True):
        resp = _analytics._analytics(req)
    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid JSON payload' in payload['message']


def test_missing_required_fields_returns_400():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    # missing measurement_id
    req = DummyRequest(headers=headers, method='POST', json_data={'client_id': 'c', 'events': [{'name': 'e'}]})
    with patch.object(_analytics, 'validate_auth_key', return_value=True):
        resp = _analytics._analytics(req)
    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing required fields' in payload['message']


def test_invalid_events_field_returns_400_for_empty_or_non_list():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}

    # events is empty list
    req_empty = DummyRequest(headers=headers, method='POST', json_data={'measurement_id': 'm', 'client_id': 'c', 'events': []})
    with patch.object(_analytics, 'validate_auth_key', return_value=True):
        resp = _analytics._analytics(req_empty)
    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing required fields' in payload['message']

    # events is not a list
    req_not_list = DummyRequest(headers=headers, method='POST', json_data={'measurement_id': 'm', 'client_id': 'c', 'events': 'nope'})
    with patch.object(_analytics, 'validate_auth_key', return_value=True):
        resp = _analytics._analytics(req_not_list)
    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "'events' field must be a non-empty list" in payload['message']


def test_secret_retrieval_failure_returns_500():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'measurement_id': 'm', 'client_id': 'c', 'events': [{'name': 'e'}]}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)
    with patch.object(_analytics, 'validate_auth_key', return_value=True), patch.object(_analytics, 'get_secret_key', side_effect=Exception('boom')):
        resp = _analytics._analytics(req)
    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Could not retrieve GA secret' in payload['message']


def test_successful_flow_calls_httpx_with_expected_url_and_payload():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    measurement_id = 'MEAS_ABC'
    client_id = 'roksta_console'
    events = [{'name': 'evt', 'params': {'a': 1}}]
    user_id = 'user-123'
    req_payload = {'measurement_id': measurement_id, 'client_id': client_id, 'events': events, 'user_id': user_id}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Recording client to capture call details
    class RecordingClient:
        def __init__(self):
            self.post_called = False
            self.last_url = None
            self.last_json = None
            self.last_timeout = None

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, url, json=None, timeout=30):
            self.post_called = True
            self.last_url = url
            self.last_json = json
            self.last_timeout = timeout
            resp = Mock()
            resp.raise_for_status = Mock(return_value=None)
            resp.status_code = 200
            resp.text = ''
            return resp

    recording = RecordingClient()

    with patch.object(_analytics, 'validate_auth_key', return_value=True), \
         patch.object(_analytics, 'get_secret_key', return_value='GA-SECRET'), \
         patch.object(_analytics.httpx, 'Client', return_value=recording):
        resp = _analytics._analytics(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True

    expected_url = f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret=GA-SECRET"
    assert recording.post_called is True
    assert recording.last_url == expected_url
    assert recording.last_json['client_id'] == client_id
    assert recording.last_json['events'] == events
    assert recording.last_json['user_id'] == user_id


def test_httpx_http_status_error_is_logged_but_function_returns_200():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'measurement_id': 'm', 'client_id': 'c', 'events': [{'name': 'e'}]}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Client that returns a response whose raise_for_status raises HTTPStatusError
    class ErrClient1:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, url, json=None, timeout=30):
            resp = Mock()
            # Raise a fake HTTPStatusError instance with a response attribute
            resp.raise_for_status = Mock(side_effect=_analytics.httpx.HTTPStatusError(Mock(status_code=400, text='bad')))
            resp.status_code = 400
            resp.text = 'bad'
            return resp

    err_client = ErrClient1()

    with patch.object(_analytics, 'validate_auth_key', return_value=True), \
         patch.object(_analytics, 'get_secret_key', return_value='GA-SECRET'), \
         patch.object(_analytics.httpx, 'Client', return_value=err_client):
        resp = _analytics._analytics(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True


def test_httpx_request_error_is_logged_but_function_returns_200():
    headers = {_analytics.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'measurement_id': 'm', 'client_id': 'c', 'events': [{'name': 'e'}]}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Client whose post itself raises a RequestError
    class ErrClient2:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def post(self, url, json=None, timeout=30):
            raise _analytics.httpx.RequestError('network')

    err_client = ErrClient2()

    with patch.object(_analytics, 'validate_auth_key', return_value=True), \
         patch.object(_analytics, 'get_secret_key', return_value='GA-SECRET'), \
         patch.object(_analytics.httpx, 'Client', return_value=err_client):
        resp = _analytics._analytics(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
