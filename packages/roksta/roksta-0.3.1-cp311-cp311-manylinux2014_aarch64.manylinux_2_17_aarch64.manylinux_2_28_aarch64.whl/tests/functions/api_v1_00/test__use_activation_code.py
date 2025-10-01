import os
import sys
import json
import types
import importlib
from unittest.mock import patch
from datetime import datetime, timezone, timedelta

# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# -----------------------------
# Provide lightweight fake modules to satisfy imports inside _use_activation_code
# These are minimal and will be patched in individual tests as needed.
# -----------------------------
# Save original sys.modules entries so we can restore them after importing the module under test
_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'utils',
    'auth',
    'firebase_admin',
    'firebase_admin.firestore',
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

# Fake utils module (create_json_response, verify_firebase_token)
utils_mod = types.ModuleType('utils')


def _fake_create_json_response(success: bool, payload: any, status_code: int):
    response_body = {"success": success, "payload": payload}
    return firebase_functions.https_fn.Response(response=response_body, status=status_code, headers={'Content-Type': 'application/json'})


def _fake_verify_firebase_token(req):
    # Default: successful verification returning a uid
    return {'uid': 'user_1'}


utils_mod.create_json_response = _fake_create_json_response
utils_mod.verify_firebase_token = _fake_verify_firebase_token
sys.modules['utils'] = utils_mod

# Fake top-level auth module (validate_auth_key will be patched per-test as needed)
auth_mod = types.ModuleType('auth')


def _simple_validate_auth_key(val: str) -> bool:
    return bool(val)


auth_mod.validate_auth_key = _simple_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake firebase_admin.firestore using an in-memory dict
firebase_admin_mod = types.ModuleType('firebase_admin')

# In-memory fake DB used by the fake Firestore implementation
fake_db_data = {}

class DocumentSnapshot:
    def __init__(self, exists, data):
        self.exists = exists
        self._data = data

    def to_dict(self):
        return self._data

    def get(self, key):
        if not self._data:
            return None
        return self._data.get(key)


class DocumentRef:
    def __init__(self, collection_name, doc_id):
        self.collection = collection_name
        self.doc_id = doc_id

    def get(self, transaction=None):
        coll = fake_db_data.get(self.collection, {})
        if self.doc_id in coll:
            return DocumentSnapshot(True, coll[self.doc_id])
        return DocumentSnapshot(False, None)

    def update(self, update_dict):
        coll = fake_db_data.setdefault(self.collection, {})
        doc = coll.setdefault(self.doc_id, {})
        if isinstance(doc, dict):
            doc.update(update_dict)
        else:
            coll[self.doc_id] = update_dict

    def set(self, data):
        coll = fake_db_data.setdefault(self.collection, {})
        coll[self.doc_id] = data


class CollectionRef:
    def __init__(self, name):
        self.name = name

    def document(self, doc_id):
        return DocumentRef(self.name, doc_id)


class FakeTransaction:
    def __init__(self):
        pass

    def update(self, doc_ref, update_dict):
        coll = fake_db_data.setdefault(doc_ref.collection, {})
        doc = coll.setdefault(doc_ref.doc_id, {})
        if isinstance(doc, dict):
            doc.update(update_dict)
        else:
            coll[doc_ref.doc_id] = update_dict

    def set(self, doc_ref, data):
        coll = fake_db_data.setdefault(doc_ref.collection, {})
        coll[doc_ref.doc_id] = data


class FakeFirestoreClient:
    def __init__(self):
        pass

    def collection(self, name):
        return CollectionRef(name)

    def transaction(self):
        return FakeTransaction()


fake_firestore_mod = types.ModuleType('firebase_admin.firestore')
fake_firestore_mod.client = lambda: FakeFirestoreClient()
fake_firestore_mod.transactional = lambda f: f
fake_firestore_mod.SERVER_TIMESTAMP = object()
sys.modules['firebase_admin.firestore'] = fake_firestore_mod
firebase_admin_mod.firestore = fake_firestore_mod
sys.modules['firebase_admin'] = firebase_admin_mod

# -----------------------------
# Import the module under test after preparing the fake imports
# -----------------------------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_use_activation_code.py')
spec = importlib.util.spec_from_file_location('api_v1_00._use_activation_code', module_path)
_use_activation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_use_activation)


# Restore original sys.modules mappings to avoid side-effects for other tests
for name, orig in _orig_sys_modules.items():
    if orig is None:
        try:
            del sys.modules[name]
        except KeyError:
            pass
    else:
        sys.modules[name] = orig

# Import env constants for auth header usage in tests
import env as functions_env  # noqa: E402
AUTH_HEADER_NAME = functions_env.AUTH_HEADER_NAME


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
    fake_db_data.clear()
    req = DummyRequest(headers={}, method='POST')
    # Ensure token verification isn't called when header missing
    with patch.object(_use_activation, 'verify_firebase_token', side_effect=Exception('Should not be called')):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['payload']


def test_invalid_auth_key_returns_403():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'bad-token'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_use_activation, 'validate_auth_key', return_value=False):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['payload']


def test_verify_firebase_token_failure_returns_403():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', side_effect=Exception('boom')):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Authentication failed' in payload['payload']


def test_missing_json_payload_returns_400():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data=None)
    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid or missing JSON payload' in payload['payload']


def test_missing_activation_code_returns_400():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'ok'}
    # Provide a non-empty JSON payload without 'activation_code' to trigger the missing key branch
    req = DummyRequest(headers=headers, method='POST', json_data={'foo': 'bar'})
    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert "Missing 'activation_code'" in payload['payload']


def test_user_does_not_exist_returns_404():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'code1'})
    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 404
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'User does not exist' in payload['payload']


def test_user_already_active_returns_200():
    fake_db_data.clear()
    fake_db_data.setdefault('users', {})['user_1'] = {'active': True}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'code1'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'Account is already active' in payload['payload']


def test_activation_code_not_found_returns_404():
    fake_db_data.clear()
    # user exists and inactive
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'CodeX'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 404
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid activation code' in payload['payload']


def test_activation_code_missing_expiry_returns_500():
    fake_db_data.clear()
    # user exists and inactive
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}
    # activation code exists but missing expiry_date
    fake_db_data.setdefault('activation_codes', {})['codea'] = {'use_count': 0, 'max_uses': 1}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'codeA'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Activation code expiry information is missing' in payload['payload']


def test_activation_code_expired_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}
    past = datetime.now(timezone.utc) - timedelta(days=1)
    fake_db_data.setdefault('activation_codes', {})['expiredcode'] = {'expiry_date': past, 'use_count': 0, 'max_uses': 5}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'expiredCode'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Activation code has expired' in payload['payload']


def test_activation_code_usage_limit_reached_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}
    fake_db_data.setdefault('activation_codes', {})['limitcode'] = {'expiry_date': datetime.now(timezone.utc) + timedelta(days=1), 'use_count': 5, 'max_uses': 5}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'limitCode'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Usage limit has been hit' in payload['payload']


def test_user_already_used_code_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}
    code = 'multi'
    fake_db_data.setdefault('activation_codes', {})[code] = {'expiry_date': datetime.now(timezone.utc) + timedelta(days=1), 'use_count': 0, 'max_uses': 5}
    # Create an activation record indicating user already used the code
    fake_db_data.setdefault('activations', {})[f"{code}_user_1"] = {'activation_code': code, 'user_id': 'user_1', 'timestamp': fake_firestore_mod.SERVER_TIMESTAMP}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'MULTI'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'User has already used this activation code' in payload['payload']


def test_successful_activation_returns_200_and_updates_db():
    fake_db_data.clear()
    fake_db_data.setdefault('users', {})['user_1'] = {'active': False}
    code = 'successcode'
    fake_db_data.setdefault('activation_codes', {})[code] = {'expiry_date': datetime.now(timezone.utc) + timedelta(days=1), 'use_count': 2, 'max_uses': 5}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'activation_code': 'SuccessCode'})

    with patch.object(_use_activation, 'validate_auth_key', return_value=True), patch.object(_use_activation, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _use_activation._use_activation_code(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'Activation code used successfully' in payload['payload']

    # Verify database updates
    user_doc = fake_db_data.get('users', {}).get('user_1')
    assert user_doc is not None
    assert user_doc.get('active') is True

    code_doc = fake_db_data.get('activation_codes', {}).get(code)
    assert code_doc is not None
    assert code_doc.get('use_count') == 3

    activation_key = f"{code}_user_1"
    activations = fake_db_data.get('activations', {})
    assert activation_key in activations
    act = activations[activation_key]
    assert act['user_id'] == 'user_1'
    assert act['activation_code'] == code
    assert 'timestamp' in act
    # timestamp should be the firestore.SERVER_TIMESTAMP sentinel
    assert act['timestamp'] is fake_firestore_mod.SERVER_TIMESTAMP
