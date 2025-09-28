import importlib
import sys
import types
import json
import pytest


def _setup_basic_stubs(secret_data=b'MY_SECRET', secret_side_effect=None, auth_verify=lambda token: {'uid': 'u1'}):
    """Install minimal stub modules for google.cloud.secretmanager, firebase_functions and firebase_admin.
    Returns a dict of original sys.modules entries for cleanup.
    """
    orig = {}
    names = [
        'google',
        'google.cloud',
        'google.cloud.secretmanager',
        'firebase_functions',
        'firebase_admin',
        'firebase_admin.auth',
    ]
    for name in names:
        orig[name] = sys.modules.get(name)

    # google package and submodules
    google_mod = types.ModuleType('google')
    cloud_mod = types.ModuleType('google.cloud')
    secretmanager_mod = types.ModuleType('google.cloud.secretmanager')

    class _Payload:
        def __init__(self, data):
            self.data = data

    class _Response:
        def __init__(self, data):
            self.payload = _Payload(data)

    class SecretManagerServiceClient:
        def access_secret_version(self, request=None):
            if secret_side_effect:
                # raise the provided exception instance for testing
                raise secret_side_effect
            return _Response(secret_data)

    secretmanager_mod.SecretManagerServiceClient = SecretManagerServiceClient
    cloud_mod.secretmanager = secretmanager_mod
    google_mod.cloud = cloud_mod

    sys.modules['google'] = google_mod
    sys.modules['google.cloud'] = cloud_mod
    sys.modules['google.cloud.secretmanager'] = secretmanager_mod

    # firebase_functions stub with a Response type expected by utils.create_json_response
    firebase_functions_mod = types.ModuleType('firebase_functions')

    class FakeResponse:
        def __init__(self, response=None, mimetype=None, status=200, **kwargs):
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

    firebase_functions_mod.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
    sys.modules['firebase_functions'] = firebase_functions_mod

    # firebase_admin + auth stub
    firebase_admin_mod = types.ModuleType('firebase_admin')
    auth_mod = types.ModuleType('firebase_admin.auth')

    def _verify_id_token(token):
        return auth_verify(token)

    auth_mod.verify_id_token = _verify_id_token
    firebase_admin_mod.auth = auth_mod
    sys.modules['firebase_admin'] = firebase_admin_mod
    sys.modules['firebase_admin.auth'] = auth_mod

    return orig


def _restore_orig(orig):
    for name, val in orig.items():
        if val is None:
            if name in sys.modules:
                del sys.modules[name]
        else:
            sys.modules[name] = val


def test_get_secret_key_returns_decoded_string_on_success():
    orig = _setup_basic_stubs(secret_data=b'MY_SECRET')
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')
        res = utils.get_secret_key('any')
        assert res == 'MY_SECRET'
    finally:
        _restore_orig(orig)


def test_get_secret_key_raises_exception_on_client_error():
    orig = _setup_basic_stubs(secret_side_effect=Exception('boom'))
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')
        with pytest.raises(Exception) as exc:
            utils.get_secret_key('any')
        assert 'Failed to retrieve secret key' in str(exc.value)
        assert 'boom' in str(exc.value)
    finally:
        _restore_orig(orig)


def test_verify_firebase_token_raises_when_header_missing_or_invalid():
    orig = _setup_basic_stubs()
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')

        class DummyRequest:
            def __init__(self, headers=None):
                self.headers = headers or {}

        # Missing header
        req = DummyRequest(headers={})
        with pytest.raises(Exception) as exc:
            utils.verify_firebase_token(req)
        assert 'Missing or invalid Authorization header' in str(exc.value)

        # Header present but not starting with 'Bearer '
        req2 = DummyRequest(headers={'Authorization': 'Token abc'})
        with pytest.raises(Exception) as exc2:
            utils.verify_firebase_token(req2)
        assert 'Missing or invalid Authorization header' in str(exc2.value)
    finally:
        _restore_orig(orig)


def test_verify_firebase_token_calls_auth_verify_and_returns_payload():
    orig = _setup_basic_stubs(auth_verify=lambda token: {'uid': 'user_1'})
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')

        class DummyRequest:
            def __init__(self, headers=None):
                self.headers = headers or {}

        req = DummyRequest(headers={'Authorization': 'Bearer TOK'})
        res = utils.verify_firebase_token(req)
        assert res == {'uid': 'user_1'}
    finally:
        _restore_orig(orig)


def test_verify_firebase_token_wraps_auth_exceptions():
    def _raiser(token):
        raise Exception('bad token')

    orig = _setup_basic_stubs(auth_verify=_raiser)
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')

        class DummyRequest:
            def __init__(self, headers=None):
                self.headers = headers or {}

        req = DummyRequest(headers={'Authorization': 'Bearer TOK'})
        with pytest.raises(Exception) as exc:
            utils.verify_firebase_token(req)
        assert 'Authentication failed' in str(exc.value)
        assert 'bad token' in str(exc.value)
    finally:
        _restore_orig(orig)


def test_get_api_key_uses_lowercase_family_name_and_get_secret_key(monkeypatch):
    orig = _setup_basic_stubs()
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')

        called = {}

        def fake_get_secret_key(name):
            called['name'] = name
            return 'THE_KEY'

        monkeypatch.setattr(utils, 'get_secret_key', fake_get_secret_key)
        from enums import LlmFamily
        res = utils.get_api_key(LlmFamily.OPENAI)
        assert res == 'THE_KEY'
        assert called['name'] == 'openai-api-key'
    finally:
        _restore_orig(orig)


def test_create_json_response_returns_formatted_response():
    orig = _setup_basic_stubs()
    try:
        if 'utils' in sys.modules:
            del sys.modules['utils']
        utils = importlib.import_module('utils')
        resp = utils.create_json_response(True, {'a': 1}, 201)
        assert getattr(resp, 'status_code', None) == 201
        data = json.loads(resp.get_data(as_text=True))
        assert data == {"success": True, "payload": {"a": 1}}
    finally:
        _restore_orig(orig)
