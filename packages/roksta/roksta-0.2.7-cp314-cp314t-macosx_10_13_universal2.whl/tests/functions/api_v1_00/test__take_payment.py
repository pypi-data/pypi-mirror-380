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
# Provide lightweight fake modules to satisfy imports inside _take_payment
# These are minimal and will be patched in individual tests as needed.
# -----------------------------
# Save original sys.modules entries so we can restore them after importing the module under test
_orig_sys_modules = {}
_names_to_fake = [
    'firebase_functions',
    'utils',
    'auth',
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

# Fake utils module (create_json_response, get_secret_key, verify_firebase_token)
utils_mod = types.ModuleType('utils')


def _fake_create_json_response(success: bool, payload: any, status_code: int):
    response_body = {"success": success, "payload": payload}
    return firebase_functions.https_fn.Response(response=response_body, status=status_code, headers={'Content-Type': 'application/json'})


def _fake_get_secret_key(name: str) -> str:
    return 'DUMMY_STRIPE_KEY'


def _fake_verify_firebase_token(req):
    # Default: successful verification returning a uid
    return {'uid': 'user_1'}


utils_mod.create_json_response = _fake_create_json_response
utils_mod.get_secret_key = _fake_get_secret_key
utils_mod.verify_firebase_token = _fake_verify_firebase_token
sys.modules['utils'] = utils_mod

# Fake top-level auth module (validate_auth_key will be patched per-test as needed)
auth_mod = types.ModuleType('auth')

def _simple_validate_auth_key(val: str) -> bool:
    return True


auth_mod.validate_auth_key = _simple_validate_auth_key
sys.modules['auth'] = auth_mod

# Fake firebase_admin.auth and firebase_admin.firestore
firebase_admin_mod = types.ModuleType('firebase_admin')

# firebase_admin.auth fake
fauth_mod = types.ModuleType('firebase_admin.auth')

def _fake_get_user(uid):
    return types.SimpleNamespace(email='user@example.com')

fauth_mod.get_user = _fake_get_user
sys.modules['firebase_admin.auth'] = fauth_mod
firebase_admin_mod.auth = fauth_mod

# In-memory fake DB used by the fake Firestore implementation
fake_db_data = {}

# Fake Firestore implementation
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

# Fake stripe module
stripe_mod = types.ModuleType('stripe')

class StripeError(Exception):
    pass

stripe_mod.error = types.SimpleNamespace(StripeError=StripeError)
stripe_mod.api_key = None

class _PaymentIntent:
    @staticmethod
    def create(**kwargs):
        raise NotImplementedError("PaymentIntent.create not implemented for test stub")

stripe_mod.PaymentIntent = _PaymentIntent
sys.modules['stripe'] = stripe_mod

# Fake ulid module
ulid_mod = types.ModuleType('ulid')
ulid_mod.new = lambda: 'ULID123'
sys.modules['ulid'] = ulid_mod

# -----------------------------
# Import the module under test after preparing the fake imports
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_00', '_take_payment.py')
spec = importlib.util.spec_from_file_location('api_v1_00._take_payment', module_path)
_take_payment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_take_payment)


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
    req = DummyRequest(headers={}, method='POST')
    resp = _take_payment._take_payment(req)

    assert resp.status_code == 401
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing app authentication key' in payload['payload']


def test_invalid_auth_key_returns_403():
    headers = {AUTH_HEADER_NAME: 'bad-token'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_take_payment, 'validate_auth_key', return_value=False):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid app authentication key' in payload['payload']


def test_verify_firebase_token_failure_returns_403():
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST')
    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', side_effect=Exception('boom')):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 403
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Authentication failed' in payload['payload']


def test_missing_json_payload_returns_400():
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data=None)
    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'No JSON payload provided' in payload['payload']


def test_missing_amount_returns_400():
    headers = {AUTH_HEADER_NAME: 'ok'}
    # Provide a non-empty JSON object so get_json() returns a truthy value but without 'amount'
    req = DummyRequest(headers=headers, method='POST', json_data={'foo': 'bar'})
    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing amount' in payload['payload']


def test_invalid_amount_returns_400():
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': 'not-a-number'})
    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Invalid amount value provided' in payload['payload']


def test_billing_doc_missing_returns_404():
    fake_db_data.clear()
    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})
    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 404
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Billing document does not exist' in payload['payload']


def test_missing_billing_fields_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {}

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Missing field(s) in billing document' in payload['payload']


def test_get_user_failure_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {
        'stripe_customer_id': 'cus_x',
        'stripe_payment_method_id': 'pm_x',
    }

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), \
         patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_take_payment.auth, 'get_user', side_effect=Exception('nope')):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Failed to retrieve user auth record' in payload['payload']


def test_get_secret_key_failure_returns_500():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {
        'stripe_customer_id': 'cus_x',
        'stripe_payment_method_id': 'pm_x',
    }

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), \
         patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_take_payment.auth, 'get_user', return_value=types.SimpleNamespace(email='user@example.com')), \
         patch.object(_take_payment, 'get_secret_key', side_effect=Exception('boom')):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 500
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Failed to retrieve Stripe configuration' in payload['payload']


def test_stripe_raises_StripeError_returns_400():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {
        'stripe_customer_id': 'cus_x',
        'stripe_payment_method_id': 'pm_x',
    }

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), \
         patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_take_payment.auth, 'get_user', return_value=types.SimpleNamespace(email='user@example.com')), \
         patch.object(_take_payment, 'get_secret_key', return_value='DUMMY_KEY'), \
         patch.object(_take_payment.stripe.PaymentIntent, 'create', side_effect=_take_payment.stripe.error.StripeError('fail')):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 400
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Stripe error during payment processing' in payload['payload']


def test_payment_intent_non_succeeded_returns_402():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {
        'stripe_customer_id': 'cus_x',
        'stripe_payment_method_id': 'pm_x',
    }

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    fake_resp = types.SimpleNamespace(status='requires_payment_method')

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), \
         patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_take_payment.auth, 'get_user', return_value=types.SimpleNamespace(email='user@example.com')), \
         patch.object(_take_payment, 'get_secret_key', return_value='DUMMY_KEY'), \
         patch.object(_take_payment.stripe.PaymentIntent, 'create', return_value=fake_resp):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 402
    payload = _parse_response(resp)
    assert payload['success'] is False
    assert 'Payment failed' in payload['payload']


def test_successful_payment_updates_balance_and_records_transaction_returns_200():
    fake_db_data.clear()
    fake_db_data.setdefault('billing', {})['user_1'] = {
        'stripe_customer_id': 'cus_x',
        'stripe_payment_method_id': 'pm_x',
        'balance': 5.0,
    }

    headers = {AUTH_HEADER_NAME: 'ok'}
    req = DummyRequest(headers=headers, method='POST', json_data={'amount': '10'})

    fake_payment_intent = types.SimpleNamespace(status='succeeded')

    with patch.object(_take_payment, 'validate_auth_key', return_value=True), \
         patch.object(_take_payment, 'verify_firebase_token', return_value={'uid': 'user_1'}), \
         patch.object(_take_payment.auth, 'get_user', return_value=types.SimpleNamespace(email='user@example.com')), \
         patch.object(_take_payment, 'get_secret_key', return_value='DUMMY_KEY'), \
         patch.object(_take_payment.stripe.PaymentIntent, 'create', return_value=fake_payment_intent), \
         patch.object(_take_payment.ulid, 'new', return_value='ULID123'):
        resp = _take_payment._take_payment(req)

    assert resp.status_code == 200
    payload = _parse_response(resp)
    assert payload['success'] is True
    assert 'Payment processed and balance updated successfully' in payload['payload']

    # Check that billing balance was updated
    billing_doc = fake_db_data.get('billing', {}).get('user_1')
    assert billing_doc is not None
    assert billing_doc.get('balance') == 15.0

    # Check that transaction was recorded
    transactions = fake_db_data.get('transactions', {})
    # Expect a key like 'credit_user_1_ULID123'
    matching = [k for k in transactions.keys() if k.startswith('credit_user_1_')]
    assert matching, f"No transaction created, transactions keys: {list(transactions.keys())}"
    tx = transactions[matching[0]]
    assert tx['user_id'] == 'user_1'
    assert tx['value'] == 10.0
    assert tx['balance'] == 15.0
    assert tx['type'] == 'credit'
    assert tx['reason'] == 'payment'
    assert 'timestamp' in tx
