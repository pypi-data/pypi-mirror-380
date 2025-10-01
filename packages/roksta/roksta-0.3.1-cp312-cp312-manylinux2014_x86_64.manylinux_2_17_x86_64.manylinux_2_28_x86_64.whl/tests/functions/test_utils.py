import importlib.util
import os
import sys
import types
import json
import base64
import uuid
import pytest


# Helper to create simple module stubs
def _make_fake_firebase_functions():
    fake_https = types.ModuleType('firebase_functions.https_fn')

    class FakeResponse:
        def __init__(self, response=None, mimetype=None, status=200, **kwargs):
            # Mirror the small subset of the real Response API used by the code/tests
            self.status_code = status
            if isinstance(response, bytes):
                self._text = response.decode('utf-8')
            else:
                # If a non-string is passed (unlikely), coerce to JSON text for assertions
                self._text = response if isinstance(response, str) else (json.dumps(response) if response is not None else '')
            self.mimetype = mimetype
            self.headers = {'Content-Type': mimetype} if mimetype else {}

        def get_data(self, as_text=False):
            return self._text if as_text else self._text.encode('utf-8')

    fake_https.Response = FakeResponse
    # Provide a Request attribute used in type annotations in the module under test
    fake_https.Request = types.SimpleNamespace

    fake_root = types.ModuleType('firebase_functions')
    fake_root.https_fn = fake_https
    return fake_root, fake_https


def _make_fake_firebase_admin():
    fake = types.ModuleType('firebase_admin')
    # Minimal auth object so import succeeds; tests here don't rely on actual auth behaviour
    fake.auth = types.SimpleNamespace(verify_id_token=lambda token: {'uid': 'test'})
    return fake


def _make_fake_google_secretmanager():
    google = types.ModuleType('google')
    google_cloud = types.ModuleType('google.cloud')
    secretmanager = types.ModuleType('google.cloud.secretmanager')

    class FakeClient:
        def access_secret_version(self, request):
            raise RuntimeError("SecretManager should not be called in these tests")

    secretmanager.SecretManagerServiceClient = FakeClient
    google_cloud.secretmanager = secretmanager
    google.cloud = google_cloud
    return google, google_cloud, secretmanager


def _load_utils_module(monkeypatch):
    """Load a fresh copy of functions/utils.py as an isolated module.

    This helper inserts necessary fake modules into sys.modules via the
    provided monkeypatch fixture before loading the module so its import-time
    dependencies succeed and are controllable by the tests.
    """
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    utils_path = os.path.join(repo_root, 'functions', 'utils.py')
    assert os.path.exists(utils_path), f"Expected functions/utils.py to exist at {utils_path}"

    # Prepare and register lightweight stubs needed at import time
    fake_firebase_root, fake_https = _make_fake_firebase_functions()
    monkeypatch.setitem(sys.modules, 'firebase_functions', fake_firebase_root)
    monkeypatch.setitem(sys.modules, 'firebase_functions.https_fn', fake_https)

    fake_firebase_admin = _make_fake_firebase_admin()
    monkeypatch.setitem(sys.modules, 'firebase_admin', fake_firebase_admin)

    google, google_cloud, secretmanager = _make_fake_google_secretmanager()
    monkeypatch.setitem(sys.modules, 'google', google)
    monkeypatch.setitem(sys.modules, 'google.cloud', google_cloud)
    monkeypatch.setitem(sys.modules, 'google.cloud.secretmanager', secretmanager)

    # Create a unique module name so each test gets a fresh module object
    module_name = f"tests.utils_isolated_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, utils_path)
    module = importlib.util.module_from_spec(spec)
    # Ensure the new module is discoverable under its name during execution
    monkeypatch.setitem(sys.modules, module_name, module)
    spec.loader.exec_module(module)
    return module


def test_create_json_response_returns_expected_json_and_status(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    resp = mod.create_json_response(True, {"alpha": 1}, 201)

    assert hasattr(resp, 'status_code')
    assert resp.status_code == 201

    body_text = resp.get_data(as_text=True)
    parsed = json.loads(body_text)
    assert parsed == {"success": True, "payload": {"alpha": 1}}


def test_get_sealedbox_private_key_raises_when_pynacl_privatekey_missing(monkeypatch):
    # Ensure a nacl.public module exists but does NOT expose PrivateKey so the
    # import inside get_sealedbox_private_key raises and the function reports
    # that encryption support is unavailable.
    nacl_mod = types.ModuleType('nacl')
    nacl_public = types.ModuleType('nacl.public')

    # Provide PublicKey/SealedBox but omit PrivateKey to trigger the import error
    class PublicKeyStub:
        def __init__(self, data):
            self._data = bytes(data)

    class SealedBoxStub:
        def __init__(self, key):
            pass

    nacl_public.PublicKey = PublicKeyStub
    nacl_public.SealedBox = SealedBoxStub

    monkeypatch.setitem(sys.modules, 'nacl', nacl_mod)
    monkeypatch.setitem(sys.modules, 'nacl.public', nacl_public)

    mod = _load_utils_module(monkeypatch)

    with pytest.raises(Exception) as excinfo:
        mod.get_sealedbox_private_key()

    assert 'Encryption support is unavailable' in str(excinfo.value)


def test_get_sealedbox_private_key_initializes_and_caches_private_key(monkeypatch):
    # Provide a PrivateKey implementation and stub get_secret_key to return
    # a valid 32-byte base64-encoded secret. Verify the value is cached and
    # the secret fetch is only performed once.
    key_bytes = b"\x02" * 32

    nacl_mod = types.ModuleType('nacl')
    nacl_public = types.ModuleType('nacl.public')

    class PrivateKeyStub:
        def __init__(self, data):
            # Accept bytes-like input
            self._data = bytes(data)

        def __repr__(self):
            return f"PrivateKeyStub(len={len(self._data)})"

    nacl_public.PrivateKey = PrivateKeyStub
    monkeypatch.setitem(sys.modules, 'nacl', nacl_mod)
    monkeypatch.setitem(sys.modules, 'nacl.public', nacl_public)

    mod = _load_utils_module(monkeypatch)

    calls = {'count': 0}

    def fake_get_secret_key(name):
        calls['count'] += 1
        return base64.b64encode(key_bytes).decode('ascii')

    # Replace the module-level get_secret_key with our fake
    mod.get_secret_key = fake_get_secret_key

    # Ensure fresh start
    mod._SEALEDBOX_PRIVATE_KEY = None

    first = mod.get_sealedbox_private_key()
    second = mod.get_sealedbox_private_key()

    assert first is second
    assert calls['count'] == 1
    assert hasattr(first, '_data') and first._data == key_bytes


def test_get_sealedbox_private_key_invalid_length_does_not_cache_and_raises(monkeypatch):
    # Provide PrivateKey but have the secret manager return an invalid-length key
    invalid_key = b"\x03" * 16

    nacl_mod = types.ModuleType('nacl')
    nacl_public = types.ModuleType('nacl.public')

    class PrivateKeyStub:
        def __init__(self, data):
            self._data = bytes(data)

    nacl_public.PrivateKey = PrivateKeyStub
    monkeypatch.setitem(sys.modules, 'nacl', nacl_mod)
    monkeypatch.setitem(sys.modules, 'nacl.public', nacl_public)

    mod = _load_utils_module(monkeypatch)

    def fake_get_secret_key(name):
        return base64.b64encode(invalid_key).decode('ascii')

    mod.get_secret_key = fake_get_secret_key

    # Ensure fresh start
    mod._SEALEDBOX_PRIVATE_KEY = None

    with pytest.raises(Exception) as excinfo:
        mod.get_sealedbox_private_key()

    assert 'Failed to initialize sealed-box private key' in str(excinfo.value)
    # Failure should not be cached
    assert mod._SEALEDBOX_PRIVATE_KEY is None


# ------------------------- Additional tests to improve coverage -------------------------

def test_get_secret_key_returns_secret_on_success(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    fake_payload = types.SimpleNamespace(data=b'secret-value')
    fake_response = types.SimpleNamespace(payload=fake_payload)

    class FakeClient:
        def access_secret_version(self, request):
            return fake_response

    # Patch the SecretManager client on the imported module
    monkeypatch.setattr(mod.secretmanager, 'SecretManagerServiceClient', FakeClient, raising=True)

    result = mod.get_secret_key('my-secret')
    assert result == 'secret-value'


def test_get_secret_key_raises_on_backend_error(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    class FakeClient:
        def access_secret_version(self, request):
            raise RuntimeError('boom')

    monkeypatch.setattr(mod.secretmanager, 'SecretManagerServiceClient', FakeClient, raising=True)

    with pytest.raises(Exception) as excinfo:
        mod.get_secret_key('does-not-matter')
    assert 'Failed to retrieve secret key from Secret Manager' in str(excinfo.value)


def test_verify_firebase_token_success(monkeypatch):
    mod = _load_utils_module(monkeypatch)
    req = types.SimpleNamespace(headers={'Authorization': 'Bearer SOME_TOKEN'})

    res = mod.verify_firebase_token(req)
    assert res == {'uid': 'test'}


def test_verify_firebase_token_missing_or_invalid_header_raises(monkeypatch):
    mod = _load_utils_module(monkeypatch)
    req = types.SimpleNamespace(headers={})

    with pytest.raises(Exception) as excinfo:
        mod.verify_firebase_token(req)
    # The implementation wraps the underlying message, but the cause should be present
    assert 'Missing or invalid Authorization' in str(excinfo.value)


def test_verify_firebase_token_verify_id_token_failure_raises(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    def fake_verify(token):
        raise ValueError('invalid token')

    # Replace the verifier with one that raises
    mod.auth.verify_id_token = fake_verify

    req = types.SimpleNamespace(headers={'Authorization': 'Bearer x'})
    with pytest.raises(Exception) as excinfo:
        mod.verify_firebase_token(req)
    assert 'invalid token' in str(excinfo.value)


def test_get_api_key_delegates_to_get_secret_key(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    called = {}

    def fake_get_secret_key(name):
        called['name'] = name
        return 'X'

    mod.get_secret_key = fake_get_secret_key

    result = mod.get_api_key(mod.LlmFamily.OPENAI)
    assert result == 'X'
    assert called['name'] == 'openai-api-key'


def test_get_request_json_plaintext_returns_parsed_json(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    def get_json(silent=False):
        return {'a': 1}

    req = types.SimpleNamespace(headers={}, get_json=get_json)
    result = mod.get_request_json(req, strict=False)
    assert result == {'a': 1}


def test_get_request_json_plaintext_strict_raises_on_get_json_error(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    def get_json(silent=False):
        raise ValueError('bad json')

    req = types.SimpleNamespace(headers={}, get_json=get_json)
    with pytest.raises(Exception):
        mod.get_request_json(req, strict=True)


def test_get_request_json_plaintext_non_strict_returns_none_on_get_json_error(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    def get_json(silent=False):
        raise ValueError('bad json')

    req = types.SimpleNamespace(headers={}, get_json=get_json)
    result = mod.get_request_json(req, strict=False)
    assert result is None


def _install_sealedbox_stub(monkeypatch, decrypt_behavior):
    """Helper: install a nacl.public.SealedBox stub whose decrypt returns or throws.

    decrypt_behavior may be either:
      - a bytes object to return from decrypt(), or
      - a callable that accepts ciphertext and returns bytes / raises.
    """
    nacl_mod = types.ModuleType('nacl')
    nacl_public = types.ModuleType('nacl.public')

    class SealedBox:
        def __init__(self, key):
            self._key = key

        def decrypt(self, ciphertext):
            if callable(decrypt_behavior):
                return decrypt_behavior(ciphertext)
            return decrypt_behavior

    nacl_public.SealedBox = SealedBox
    nacl_mod.public = nacl_public

    # Ensure both module paths exist in sys.modules so `from nacl.public import SealedBox` works
    monkeypatch.setitem(sys.modules, 'nacl', nacl_mod)
    monkeypatch.setitem(sys.modules, 'nacl.public', nacl_public)


def test_get_request_json_encrypted_success_using_get_data(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    plaintext = b'{"ok": true}'
    ciphertext = b'FAKECIPHERTEXT'
    body_b64 = base64.b64encode(ciphertext)

    # Request exposes get_data(as_text=False)
    def get_data(as_text=False):
        return body_b64

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, get_data=get_data)

    # SealedBox.decrypt will return the plaintext regardless of ciphertext
    _install_sealedbox_stub(monkeypatch, plaintext)
    # Stub the private key loader so it doesn't call Secret Manager
    monkeypatch.setattr(mod, 'get_sealedbox_private_key', lambda: 'DUMMY', raising=False)

    res = mod.get_request_json(req, strict=True)
    assert res == {"ok": True}


def test_get_request_json_encrypted_fallback_when_get_data_rejects_as_text_arg(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    plaintext = b'{"ok": 1}'
    ciphertext = b'CT'
    body_b64 = base64.b64encode(ciphertext)

    def get_data(*args, **kwargs):
        # Simulate a stub that raises when given the as_text kwarg
        if 'as_text' in kwargs:
            raise TypeError('no as_text')
        return body_b64

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, get_data=get_data)

    _install_sealedbox_stub(monkeypatch, plaintext)
    monkeypatch.setattr(mod, 'get_sealedbox_private_key', lambda: 'DUMMY', raising=False)

    res = mod.get_request_json(req, strict=True)
    assert res == {"ok": 1}


def test_get_request_json_encrypted_uses_data_attribute_if_no_get_data(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    plaintext = b'{"v": 42}'
    ciphertext = b'CT2'
    body_b64 = base64.b64encode(ciphertext)

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, data=body_b64)

    _install_sealedbox_stub(monkeypatch, plaintext)
    monkeypatch.setattr(mod, 'get_sealedbox_private_key', lambda: 'DUMMY', raising=False)

    res = mod.get_request_json(req, strict=True)
    assert res == {"v": 42}


def test_get_request_json_encrypted_invalid_base64(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    # Make b64 decoder throw to exercise that error path deterministically
    def fake_b64decode(_):
        raise Exception('bad base64')

    monkeypatch.setattr(mod.base64, 'b64decode', fake_b64decode, raising=True)

    def get_data(as_text=False):
        return b'NOT-BASE64'

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, get_data=get_data)

    # Non-strict should return None
    res = mod.get_request_json(req, strict=False)
    assert res is None

    # Strict should raise
    with pytest.raises(Exception):
        mod.get_request_json(req, strict=True)


def test_get_request_json_encrypted_decrypt_failure(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    ciphertext = b'CT'
    body_b64 = base64.b64encode(ciphertext)

    # SealedBox.decrypt will raise to simulate decryption failure
    def raise_on_decrypt(_):
        raise RuntimeError('bad decrypt')

    _install_sealedbox_stub(monkeypatch, raise_on_decrypt)
    monkeypatch.setattr(mod, 'get_sealedbox_private_key', lambda: 'DUMMY', raising=False)

    def get_data(as_text=False):
        return body_b64

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, get_data=get_data)

    # Non-strict returns None
    assert mod.get_request_json(req, strict=False) is None

    # Strict raises
    with pytest.raises(Exception):
        mod.get_request_json(req, strict=True)


def test_get_request_json_encrypted_invalid_json_after_decrypt(monkeypatch):
    mod = _load_utils_module(monkeypatch)

    # Decrypt returns bytes that are not valid JSON
    _install_sealedbox_stub(monkeypatch, b'not-json')
    monkeypatch.setattr(mod, 'get_sealedbox_private_key', lambda: 'DUMMY', raising=False)

    body_b64 = base64.b64encode(b'CT')

    def get_data(as_text=False):
        return body_b64

    req = types.SimpleNamespace(headers={mod.ENCRYPTION_HEADER_NAME: 'true'}, get_data=get_data)

    assert mod.get_request_json(req, strict=False) is None
    with pytest.raises(Exception):
        mod.get_request_json(req, strict=True)


# End of additional tests
