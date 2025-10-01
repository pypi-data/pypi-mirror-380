import importlib
from cryptography.fernet import Fernet


def test_validate_auth_key_returns_true_for_valid_token():
    """Encrypt the known AUTH_KEY with the module's FERNET_KEY and verify validation passes."""
    auth = importlib.import_module('auth')
    cipher = Fernet(auth.FERNET_KEY)
    token = cipher.encrypt(auth.AUTH_KEY.encode()).decode('utf-8')
    assert auth.validate_auth_key(token) is True


def test_validate_auth_key_returns_false_for_invalid_token_string():
    """Passing a non-Fernet string should return False rather than raise."""
    auth = importlib.import_module('auth')
    assert auth.validate_auth_key('not-a-token') is False


def test_validate_auth_key_returns_false_for_wrong_plaintext():
    """Encrypting a different plaintext with the correct key should not validate."""
    auth = importlib.import_module('auth')
    cipher = Fernet(auth.FERNET_KEY)
    token = cipher.encrypt(b'WRONG').decode('utf-8')
    assert auth.validate_auth_key(token) is False
