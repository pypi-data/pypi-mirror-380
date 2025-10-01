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

# -----------------------------
# Provide lightweight fake modules to satisfy imports inside _redeem_credit_code
# These are minimal and will be patched in individual tests as needed.
# -----------------------------
# Save original sys.modules entries so we can restore them after importing the module under test
_orig_sys_modules = {}
_names_to_fake = ['firebase_functions', 'utils', 'auth', 'firebase_admin']
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

# Fake utils module (verify_firebase_token, create_json_response)
utils_mod = types.ModuleType('utils')

def _dummy_verify_firebase_token(req: object) -> dict:
    # Default behavior: return a decoded token with a uid
    return {'uid': 'test_user'}

def _create_json_response(success: bool, payload=None, status_code: int = 200):
    # Normalize payload to include a message field
    if isinstance(payload, dict):
        message = payload.get('message', '')
        data = {'success': success, 'message': message}
        # include rest of payload under 'payload' to mirror production structure
        data['payload'] = payload
    else:
        message = payload if payload is not None else ''
        data = {'success': success, 'message': message}
    # Use the fake firebase_functions response object
    return firebase_functions.https_fn.Response(response=data, status=status_code)

utils_mod.verify_firebase_token = _dummy_verify_firebase_token
utils_mod.create_json_response = _create_json_response
sys.modules['utils'] = utils_mod

# Fake auth module (validate_auth_key will be patched per-test as needed)
auth_mod = types.ModuleType('auth')

def _simple_validate_auth_key(val: str) -> bool:
    return bool(val)

auth_mod.validate_auth_key = _simple_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake firebase_admin to prevent importing the real package during tests
firebase_admin = types.ModuleType('firebase_admin')
# Minimal fake firestore object with attributes referenced by the function
fake_firestore = types.SimpleNamespace(
    client=lambda: None,
    transactional=lambda f: f,
    SERVER_TIMESTAMP=None
)
firebase_admin.firestore = fake_firestore
sys.modules['firebase_admin'] = firebase_admin

# -----------------------------
# Import the module under test after preparing the fake imports
# -----------------------------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_redeem_credit_code.py')
spec = importlib.util.spec_from_file_location('api_v1_00._redeem_credit_code', module_path)
_redeem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_redeem)


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

    def get_json(self, silent=True):
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
    # Ensure verify_firebase_token is not called when header is missing
    with patch.object(_redeem, 'verify_firebase_token', side_effect=Exception('Should not be called')):
        resp = _redeem._redeem_credit_code(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing authentication key' in payload['message']


def test_invalid_auth_key_returns_403():
    headers = {_redeem.AUTH_HEADER_NAME: 'bad-token'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_redeem, 'validate_auth_key', return_value=False):
        resp = _redeem._redeem_credit_code(req)
    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid authentication key' in payload['message']


def test_valid_auth_key_passes_and_proceeds():
    headers = {_redeem.AUTH_HEADER_NAME: 'ok'}
    # Provide an empty JSON payload to trigger the existing JSON validation path
    req = DummyRequest(headers=headers, method='POST', json_data={})
    with patch.object(_redeem, 'validate_auth_key', return_value=True):
        resp = _redeem._redeem_credit_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid or missing JSON payload' in payload['message']
