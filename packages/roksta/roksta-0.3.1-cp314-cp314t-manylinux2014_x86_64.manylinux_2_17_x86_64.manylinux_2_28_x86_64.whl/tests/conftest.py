import os
import sys
import importlib
import types as _types_mod

# Ensure local package is imported before any globally installed packages.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure functions directory is on sys.path so top-level function helpers (e.g. 'utils')
# can be imported by tests after the functions/ reorganisation.
_functions_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions'))
if _functions_root not in sys.path:
    sys.path.insert(0, _functions_root)

# Ensure functions/api_v0_01 (or a compatible API directory) is on sys.path so tests that import top-level function
# modules (e.g. '_analytics') can still find them after the functions/ reorganisation.
_api_candidates = ['api_v0_01', 'api_v001', 'api_v0_1', 'api_v01']
_functions_api_dir = None
for candidate in _api_candidates:
    candidate_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions', candidate))
    if os.path.isdir(candidate_path):
        _functions_api_dir = candidate_path
        break
if _functions_api_dir and _functions_api_dir not in sys.path:
    sys.path.insert(0, _functions_api_dir)

# Provide a minimal google.genai.types stub if the real package is not available.
# This avoids import-time errors in tests that import modules which reference
# google.genai.types at import time. The stub is intentionally lightweight and
# only implements the attributes needed for import and simple spec-based mocks
# used in the test-suite. Individual tests may still override these with more
# detailed fakes when required.


def _attach_gtypes_stubs(gtypes_mod):
    """
    Attach minimal placeholder implementations to the provided module object.
    Only attaches attributes that are missing on the module to avoid clobbering
    a real installed package.
    """
    # Minimal placeholder implementations
    class GenerateContentConfig:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.kwargs = kwargs
        def to_json_dict(self):
            return dict(self.kwargs)

    class ThinkingConfig:
        def __init__(self, thinking_budget=None):
            self.thinking_budget = thinking_budget

    class AutomaticFunctionCallingConfig:
        def __init__(self, disable=False):
            self.disable = disable

    class GoogleSearch:
        def __init__(self):
            pass

    class Tool:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    class UsageMetadata:
        def __init__(self, prompt_token_count=0, total_token_count=0):
            self.prompt_token_count = prompt_token_count
            self.total_token_count = total_token_count

    class FinishReasonEnum:
        def __init__(self, name='FINISH_REASON_UNSPECIFIED'):
            self.name = name

    class FinishReason:
        FINISH_REASON_UNSPECIFIED = FinishReasonEnum('FINISH_REASON_UNSPECIFIED')

    class Part:
        def __init__(self, text=None, function_call=None):
            self.text = text
            self.function_call = function_call

        @classmethod
        def from_function_response(cls, name=None, response=None):
            inst = cls()
            inst.function_response = _types_mod.SimpleNamespace(name=name, response=response)
            return inst

    class Content:
        def __init__(self, role=None, parts=None):
            self.role = role
            self.parts = parts or []

        def model_dump(self, mode='json'):
            return {'role': self.role, 'parts': [getattr(p, 'text', p) for p in self.parts]}

    class FunctionCall:
        def __init__(self, name=None, args=None):
            self.name = name
            self.args = args

    class Candidate:
        def __init__(self, content=None, finish_reason=None):
            self.content = content
            self.finish_reason = finish_reason

    class GenerateContentResponse:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
            # sensible defaults
            if not hasattr(self, 'text'):
                self.text = ''
            if not hasattr(self, 'candidates'):
                self.candidates = []
            if not hasattr(self, 'usage_metadata'):
                self.usage_metadata = None

        def to_json_dict(self):
            return {k: getattr(self, k) for k in self.__dict__}

    stubs = {
        'GenerateContentConfig': GenerateContentConfig,
        'ThinkingConfig': ThinkingConfig,
        'AutomaticFunctionCallingConfig': AutomaticFunctionCallingConfig,
        'GoogleSearch': GoogleSearch,
        'Tool': Tool,
        'UsageMetadata': UsageMetadata,
        'FinishReason': FinishReason,
        'Part': Part,
        'Content': Content,
        'FunctionCall': FunctionCall,
        'Candidate': Candidate,
        'GenerateContentResponse': GenerateContentResponse,
    }

    for name, obj in stubs.items():
        if not hasattr(gtypes_mod, name):
            setattr(gtypes_mod, name, obj)


# Try to import the real google.genai.types module. If it exists, only patch in
# any missing attributes. If it doesn't exist, create minimal stub modules and
# register them on sys.modules so imports like `from google.genai import types`
# work during the tests.
try:
    gtypes = importlib.import_module('google.genai.types')
    _attach_gtypes_stubs(gtypes)
except Exception:
    # Ensure top-level `google` module exists in sys.modules, but do not overwrite
    # a real `google` module if it is already installed.
    try:
        google = importlib.import_module('google')
    except Exception:
        google = _types_mod.ModuleType('google')
        sys.modules['google'] = google

    # Ensure `google.genai` exists; prefer the real module if present.
    try:
        genai = importlib.import_module('google.genai')
    except Exception:
        genai = _types_mod.ModuleType('google.genai')
        sys.modules['google.genai'] = genai
        setattr(google, 'genai', genai)

    # Create and attach the minimal `google.genai.types` stub
    gtypes = _types_mod.ModuleType('google.genai.types')
    _attach_gtypes_stubs(gtypes)
    genai.types = gtypes
    sys.modules['google.genai.types'] = gtypes

# Provide a minimal nacl.public stub if PyNaCl is not installed. This prevents
# import-time failures in tests that import `roksta.firebase` which does
# `from nacl.public import PublicKey, SealedBox`.
try:
    import nacl.public  # type: ignore
except Exception:
    # Create lightweight stub modules to satisfy `from nacl.public import PublicKey, SealedBox`
    nacl = _types_mod.ModuleType('nacl')
    nacl_public = _types_mod.ModuleType('nacl.public')

    class PublicKey:
        def __init__(self, data):
            # Accept bytes-like input; ensure it's bytes when possible.
            try:
                self._data = bytes(data)
            except Exception:
                self._data = data

        def __repr__(self):
            try:
                length = len(self._data)
            except Exception:
                length = 'unknown'
            return f"<PublicKey len={length}>"

    class SealedBox:
        def __init__(self, public_key):
            self.public_key = public_key

        def encrypt(self, plaintext: bytes) -> bytes:
            # Return deterministic bytes so callers can base64-encode the result.
            if not isinstance(plaintext, (bytes, bytearray)):
                plaintext = str(plaintext).encode('utf-8')
            return b"STUB_ENCRYPTED:" + bytes(plaintext)

    nacl_public.PublicKey = PublicKey
    nacl_public.SealedBox = SealedBox
    # Attach the submodule on the parent module object for attribute access
    nacl.public = nacl_public
    sys.modules['nacl'] = nacl
    sys.modules['nacl.public'] = nacl_public
