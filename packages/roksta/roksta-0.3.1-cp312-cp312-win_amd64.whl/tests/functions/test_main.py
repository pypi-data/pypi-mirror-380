import importlib
import sys
import types


def test_import_initializes_firebase_and_stripe_webhook_delegates():
    # Save originals
    orig = {}
    for name in ('firebase_admin', 'firebase_functions', '_stripe_webhook', 'env', 'main'):
        orig[name] = sys.modules.get(name)

    try:
        # Stub env so DEPLOY_VERSIONS is empty and main won't try to dynamically import endpoints
        env_mod = types.ModuleType('env')
        env_mod.DEPLOY_VERSIONS = []
        sys.modules['env'] = env_mod

        # Stub firebase_admin.initialize_app and record invocation
        init_called = {'called': False}

        def fake_initialize_app():
            init_called['called'] = True

        firebase_admin_mod = types.ModuleType('firebase_admin')
        firebase_admin_mod.initialize_app = fake_initialize_app
        sys.modules['firebase_admin'] = firebase_admin_mod

        # Stub firebase_functions.https_fn.on_request decorator used by main
        def on_request(memory=None, timeout_sec=None):
            def decorator(fn):
                # return the function unchanged; this keeps behavior simple for testing
                return fn
            return decorator

        firebase_functions_mod = types.ModuleType('firebase_functions')
        firebase_functions_mod.https_fn = types.SimpleNamespace(on_request=on_request, Request=object, Response=object)
        sys.modules['firebase_functions'] = firebase_functions_mod

        # Stub the _stripe_webhook implementation that main imports
        sentinel = {'sentinel': True}

        def _stripe_webhook(req):
            return sentinel

        stripe_mod = types.ModuleType('_stripe_webhook')
        stripe_mod._stripe_webhook = _stripe_webhook
        sys.modules['_stripe_webhook'] = stripe_mod

        # Ensure main is imported fresh
        if 'main' in sys.modules:
            del sys.modules['main']

        main = importlib.import_module('main')

        # initialize_app should have been called during import
        assert init_called['called'] is True

        # The stripe_webhook exported function should delegate to our stub
        class DummyRequest:
            def __init__(self, headers=None):
                self.headers = headers or {}

        resp = main.stripe_webhook(DummyRequest())
        assert resp == sentinel

    finally:
        # Restore originals
        for name, val in orig.items():
            if val is None:
                if name in sys.modules:
                    del sys.modules[name]
            else:
                sys.modules[name] = val
