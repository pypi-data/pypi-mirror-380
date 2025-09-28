import os
import sys
import json
import types
import importlib
from unittest.mock import patch


# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# Prepare lightweight fake modules to satisfy imports inside _get_payment_details
# We'll temporarily inject these into sys.modules while importing the module

_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'utils',
    'firebase_admin',
    'firebase_admin.auth',
    'firebase_admin.firestore',
    'stripe',
    'ulid',
]
for name in _names_to_fake:
    _orig_sys_modules[name] = sys.modules.get(name)

# Fake firebase_functions.https_fn.Response to capture returned data
firebase_functions = types.ModuleType('firebase_functions')

class FakeResponse:
    def __init__(self, response=None, mimetype=None, status=200, **kwargs):
        # Mirror a small subset of the interface tests expect
        self.status_code = status
        if isinstance(response, (dict, list)):
            self._body_text = json.dumps(response)
        else:
            self._body_text = '' if response is None else response
        # Accept either a mimetype arg (used in source) or explicit headers
        self.headers = kwargs.get('headers', {})

    def get_data(self, as_text=False):
        if as_text:
            return self._body_text
        return self._body_text.encode('utf-8')

firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
sys.modules['firebase_functions'] = firebase_functions

# Fake utils module
utils_mod = types.ModuleType('utils')

# Default implementations; tests will patch attributes on the imported module when needed
def _fake_get_secret_key(name: str):
    return 'DUMMY_STRIPE_KEY'

def _fake_verify_firebase_token(req):
    # Default: successful verification
    return {'uid': 'user_1'}

# create_json_response: tests expect the payload to be merged at top-level when payload is a dict,
# or under the 'message' key when payload is a string. Return the firebase_functions.https_fn.Response
# compatible FakeResponse defined above.
def _fake_create_json_response(success: bool, payload, status_code: int):
    body = {"success": success}
    if isinstance(payload, dict):
        body.update(payload)
    else:
        body["message"] = payload
    return firebase_functions.https_fn.Response(response=body, status=status_code, mimetype="application/json")

utils_mod.get_secret_key = _fake_get_secret_key
utils_mod.verify_firebase_token = _fake_verify_firebase_token
utils_mod.create_json_response = _fake_create_json_response
sys.modules['utils'] = utils_mod

# Fake firebase_admin with auth and firestore
firebase_admin_mod = types.ModuleType('firebase_admin')

# auth fake
auth_mod = types.ModuleType('firebase_admin.auth')

def _fake_get_user(uid):
    # Return an object with an email attribute
    return types.SimpleNamespace(email='user@example.com')

auth_mod.get_user = _fake_get_user
firebase_admin_mod.auth = auth_mod
sys.modules['firebase_admin.auth'] = auth_mod

# firestore fake: minimal in-memory store for collections -> documents
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
        doc.update(update_dict)

    def set(self, data):
        coll = fake_db_data.setdefault(self.collection, {})
        coll[self.doc_id] = data

class CollectionRef:
    def __init__(self, name):
        self.name = name

    def document(self, doc_id):
        return DocumentRef(self.name, doc_id)

class FakeFirestoreClient:
    def __init__(self):
        pass

    def collection(self, name):
        return CollectionRef(name)

# Provide a minimal firestore module with client() and transactional decorator
fake_firestore_mod = types.ModuleType('firebase_admin.firestore')
fake_firestore_mod.client = lambda: FakeFirestoreClient()
# transactional decorator: just return the function unchanged in this fake
fake_firestore_mod.transactional = lambda f: f

firebase_admin_mod.firestore = fake_firestore_mod
sys.modules['firebase_admin'] = firebase_admin_mod
sys.modules['firebase_admin.firestore'] = fake_firestore_mod

# Fake stripe module
stripe_mod = types.ModuleType('stripe')

class StripeError(Exception):
    pass

stripe_mod.error = types.SimpleNamespace(StripeError=StripeError)
stripe_mod.api_key = None

class _Customer:
    @staticmethod
    def create(email=None, metadata=None):
        # Simulate creating a Stripe customer
        return types.SimpleNamespace(id='cus_new')

stripe_mod.Customer = _Customer

class _Session:
    @staticmethod
    def create(**kwargs):
        # Return a dummy checkout session
        return types.SimpleNamespace(id='sess_123', url='https://checkout.example/sess_123')

stripe_mod.checkout = types.SimpleNamespace(Session=_Session)
sys.modules['stripe'] = stripe_mod

# Fake ulid
ulid_mod = types.ModuleType('ulid')
ulid_mod.new = lambda: 'ULID123'
sys.modules['ulid'] = ulid_mod

# Import the module under test after preparing fake imports
# Load the module directly from the functions/ tree so the test's fake sys.modules entries are respected
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_get_payment_details.py')
spec = importlib.util.spec_from_file_location('api_v1_00._get_payment_details', module_path)
_get_payment_details = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_get_payment_details)

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
VALID_ENCRYPTED_KEY = functions_env.ENCRYPTED_AUTH_KEY.decode('utf-8')


# Helper request stub used in tests
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


def test_verify_firebase_token_failure_returns_403():
    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST')
    with patch.object(_get_payment_details, 'verify_firebase_token', side_effect=Exception('invalid token')):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Authentication failed' in payload.get('message', '')


def test_missing_json_payload_returns_400():
    fake_db_data.clear()
    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data=None)
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', return_value='DUMMY_STRIPE_KEY'):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid or missing JSON payload' in payload.get('message', '')


def test_billing_info_missing_returns_404():
    fake_db_data.clear()
    # provide a non-empty payload so code proceeds to check Firestore
    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', return_value='DUMMY_STRIPE_KEY'):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 404
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Billing information is missing' in payload.get('message', '')


def test_setup_session_with_existing_customer_returns_session_url():
    # Pre-populate billing doc with an existing stripe_customer_id
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {'stripe_customer_id': 'cus_existing'}

    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', return_value='DUMMY_STRIPE_KEY'):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert payload['session_url'] == 'https://checkout.example/sess_123'


def test_create_customer_and_setup_session_when_no_stripe_customer():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {}  # no stripe id

    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', return_value='DUMMY_STRIPE_KEY'):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert payload['session_url'] == 'https://checkout.example/sess_123'
    # billing doc should have been updated with new stripe_customer_id
    assert fake_db_data['billing']['user_1'].get('stripe_customer_id') == 'cus_new'


def test_get_secret_key_failure_returns_500():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {'stripe_customer_id': 'cus_existing'}

    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', side_effect=Exception('boom')):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Failed to retrieve Stripe configuration' in payload.get('message', '')


def test_invalid_negative_amount_returns_400():
    # Ensure billing doc exists so code reaches amount parsing
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {'stripe_customer_id': 'cus_existing'}

    req = DummyRequest(headers={AUTH_HEADER_NAME: VALID_ENCRYPTED_KEY, 'Authorization': 'Bearer TOK'}, method='POST', json_data={'amount': '-5'})
    with patch.object(_get_payment_details, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_get_payment_details, 'get_secret_key', return_value='DUMMY_STRIPE_KEY'):
        resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid amount value provided' in payload.get('message', '')


def test_missing_auth_header_returns_401():
    fake_db_data.clear()
    req = DummyRequest(headers={'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    # No X-Roksta-Auth-Key header provided
    resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing authentication key' in payload.get('message', '')


def test_invalid_auth_header_returns_403():
    fake_db_data.clear()
    req = DummyRequest(headers={AUTH_HEADER_NAME: 'bad-key', 'Authorization': 'Bearer TOK'}, method='POST', json_data={'dummy': True})
    resp = _get_payment_details._get_payment_details(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid authentication key' in payload.get('message', '')
