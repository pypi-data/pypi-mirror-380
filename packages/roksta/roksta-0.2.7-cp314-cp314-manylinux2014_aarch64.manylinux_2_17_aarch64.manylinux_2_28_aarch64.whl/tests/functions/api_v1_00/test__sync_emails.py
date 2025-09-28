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
# Provide lightweight fake modules to satisfy imports inside _sync_emails
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
        data['payload'] = payload
    else:
        message = payload if payload is not None else ''
        data = {'success': success, 'message': message}
    return firebase_functions.https_fn.Response(response=data, status=status_code)

utils_mod.verify_firebase_token = _dummy_verify_firebase_token
utils_mod.create_json_response = _create_json_response
sys.modules['utils'] = utils_mod

# Fake auth module (validate_auth_key will be patched per-test as needed)
auth_mod = types.ModuleType('auth')

def _simple_validate_auth_key(val: str) -> bool:
    return True

auth_mod.validate_auth_key = _simple_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake firebase_admin to prevent importing the real package during tests
firebase_admin = types.ModuleType('firebase_admin')
# Minimal fake auth and firestore objects; tests will patch their behavior as needed
fake_auth = types.SimpleNamespace(get_user=lambda uid: types.SimpleNamespace(email='test@example.com'))
# Provide a placeholder firestore client function; will be overridden by tests
fake_firestore = types.SimpleNamespace(client=lambda: None)
firebase_admin.auth = fake_auth
firebase_admin.firestore = fake_firestore
sys.modules['firebase_admin'] = firebase_admin

# -----------------------------
# Import the module under test after preparing the fake imports
# -----------------------------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_sync_emails.py')
spec = importlib.util.spec_from_file_location('api_v1_00._sync_emails', module_path)
_sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_sync)


# Restore original sys.modules mappings to avoid side-effects for other tests
for name, orig in _orig_sys_modules.items():
    if orig is None:
        try:
            del sys.modules[name]
        except KeyError:
            pass
    else:
        sys.modules[name] = orig


# -----------------------------
# Fake Firestore implementation used by tests
# -----------------------------
class FakeDocumentSnapshot:
    def __init__(self, exists: bool, data: dict | None):
        self.exists = exists
        self._data = data

    def to_dict(self):
        return self._data


class FakeDocumentReference:
    def __init__(self, client, collection: str, doc_id: str):
        self.client = client
        self.collection = collection
        self.doc_id = doc_id

    def get(self):
        coll = self.client._data.get(self.collection, {})
        if self.doc_id in coll:
            return FakeDocumentSnapshot(True, coll[self.doc_id])
        return FakeDocumentSnapshot(False, None)

    def update(self, update_dict: dict):
        # Record the update
        self.client._updates.append((self.collection, self.doc_id, update_dict))
        coll = self.client._data.setdefault(self.collection, {})
        # Apply update to stored doc if it exists and is a dict
        if isinstance(coll.get(self.doc_id), dict):
            coll[self.doc_id].update(update_dict)
        else:
            coll[self.doc_id] = update_dict


class FakeCollectionReference:
    def __init__(self, client, name: str):
        self.client = client
        self.name = name

    def document(self, doc_id: str):
        return FakeDocumentReference(self.client, self.name, doc_id)


class FakeFirestoreClient:
    def __init__(self, initial_data: dict | None = None):
        # initial_data should be a dict mapping collection_name -> {doc_id: doc_data}
        self._data = initial_data.copy() if initial_data else {}
        self._updates = []

    def collection(self, name: str):
        return FakeCollectionReference(self, name)

    def get_updates(self):
        return self._updates


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
    with patch.object(_sync, 'verify_firebase_token', side_effect=Exception('Should not be called')):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['message']


def test_invalid_auth_key_returns_403():
    headers = {_sync.AUTH_HEADER_NAME: 'bad-token'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_sync, 'validate_auth_key', return_value=False):
        resp = _sync._sync_emails(req)
    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['message']


def test_verify_token_raises_returns_403():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_sync, 'validate_auth_key', return_value=True), patch.object(_sync, 'verify_firebase_token', side_effect=Exception('boom')):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Authentication failed' in payload['message']


def test_missing_uid_in_token_returns_403():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_sync, 'validate_auth_key', return_value=True), patch.object(_sync, 'verify_firebase_token', return_value={}):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'UID missing' in payload['message']


def test_get_user_failure_returns_500():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_sync, 'validate_auth_key', return_value=True), patch.object(_sync, 'verify_firebase_token', return_value={'uid': 'u'}), patch.object(_sync.auth, 'get_user', side_effect=Exception('nope')):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Failed to retrieve user data from Firebase Authentication' in payload['message']


def test_no_updates_when_emails_match_returns_200():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')

    fake_data = {
        'users': {'u': {'email': 'auth@example.com'}},
        'billing': {'u': {'email': 'auth@example.com'}}
    }
    fake_client = FakeFirestoreClient(initial_data=fake_data)

    with patch.object(_sync, 'validate_auth_key', return_value=True), \
         patch.object(_sync, 'verify_firebase_token', return_value={'uid': 'u'}), \
         patch.object(_sync.auth, 'get_user', return_value=types.SimpleNamespace(email='auth@example.com')), \
         patch.object(_sync.firestore, 'client', return_value=fake_client):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'No email updates were necessary' in payload['message']
    assert fake_client.get_updates() == []


def test_updates_when_mismatch_calls_update_returns_200():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')

    fake_data = {
        'users': {'u': {'email': 'old_user@example.com'}},
        'billing': {'u': {'email': 'old_billing@example.com'}}
    }
    fake_client = FakeFirestoreClient(initial_data=fake_data)

    with patch.object(_sync, 'validate_auth_key', return_value=True), \
         patch.object(_sync, 'verify_firebase_token', return_value={'uid': 'u'}), \
         patch.object(_sync.auth, 'get_user', return_value=types.SimpleNamespace(email='auth@example.com')), \
         patch.object(_sync.firestore, 'client', return_value=fake_client):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'User profile email updated.' in payload['message']
    assert 'Billing email updated.' in payload['message']

    updates = fake_client.get_updates()
    # Ensure we have two updates and that both updated emails match the auth email
    assert any(u for u in updates if u[0] == 'users' and u[1] == 'u' and u[2] == {'email': 'auth@example.com'})
    assert any(u for u in updates if u[0] == 'billing' and u[1] == 'u' and u[2] == {'email': 'auth@example.com'})


def test_billing_exists_without_email_field_only_user_updated_returns_200():
    headers = {_sync.AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')

    fake_data = {
        'users': {'u': {'email': 'old_user@example.com'}},
        'billing': {'u': {'some_other_key': 'value'}}
    }
    fake_client = FakeFirestoreClient(initial_data=fake_data)

    with patch.object(_sync, 'validate_auth_key', return_value=True), \
         patch.object(_sync, 'verify_firebase_token', return_value={'uid': 'u'}), \
         patch.object(_sync.auth, 'get_user', return_value=types.SimpleNamespace(email='auth@example.com')), \
         patch.object(_sync.firestore, 'client', return_value=fake_client):
        resp = _sync._sync_emails(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'User profile email updated.' in payload['message']
    assert 'Billing email updated.' not in payload['message']

    updates = fake_client.get_updates()
    assert any(u for u in updates if u[0] == 'users' and u[1] == 'u' and u[2] == {'email': 'auth@example.com'})
    # Ensure billing was not updated
    assert not any(u for u in updates if u[0] == 'billing')
