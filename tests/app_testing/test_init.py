import sys
import types
import pytest
import logging
from app import App

def test_configure_logging_fallback(monkeypatch):
    # Make logging.config.fileConfig raise Exception
    def fake_fileConfig(path, disable_existing_loggers):
        raise Exception("fail")
    monkeypatch.setattr(logging.config, "fileConfig", fake_fileConfig)

    called = {'basicConfig': False}
    def fake_basicConfig(**kwargs):
        called['basicConfig'] = True

    monkeypatch.setattr(logging, "basicConfig", fake_basicConfig)

    app = App()
    app.configure_logging()
    assert called['basicConfig'] is True

def test_load_plugins_importerror(monkeypatch):
    original_import = __import__

    def fake_import(name, *args, **kwargs):
        if name == "app.plugins":
            raise ImportError("Simulated import error")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", fake_import)

    app = App()
    app.load_plugins()  # Should handle the simulated ImportError safely

    app = App()
    # pkgutil.iter_modules won't be called since import fails
    app.load_plugins()  # Should handle ImportError and return without error

def test_register_plugin_commands_typeerror(monkeypatch):
    app = App()
    # Dummy Command subclass
    class DummyCommand:
        def name(self):
            return "dummy"

    # command_factory.create raises TypeError
    def raise_type_error(_):
        raise TypeError()

    monkeypatch.setattr(app.command_factory, "create", raise_type_error)

    # command_handler.register_command replaced with no-op
    monkeypatch.setattr(app.command_handler, "register_command", lambda name, cmd: None)

    dummy_module = types.SimpleNamespace(DummyCommand=DummyCommand)
    app.register_plugin_commands(dummy_module, "dummy_plugin")

def test_start_keyboard_interrupt_and_finally(monkeypatch):
    app = App()
    monkeypatch.setattr(app, "load_plugins", lambda: None)

    # input raises KeyboardInterrupt immediately
    def input_raise(_):
        raise KeyboardInterrupt()
    monkeypatch.setattr("builtins.input", input_raise)

    # sys.exit replaced to raise SystemExit to test finally block
    def fake_exit(code=0):
        raise SystemExit(code)
    monkeypatch.setattr(sys, "exit", fake_exit)

    with pytest.raises(SystemExit):
        app.start()
