import logging
import pytest
from app import App

def test_config_logging(monkeypatch):
    def fake_File(path, disable_existing_loggers=False):
        raise Exception("Simulation Failure")
    monkeypatch.setattr(logging.config, "fileConfig", fake_File)

    def fake_Basic(level, format):
        called ["basic"] = (level, format)

    called = {}
    monkeypatch.setattr(logging, "basicConfig", fake_Basic)

    App().configure_logging()

    assert called["basic"][0] == logging.INFO
    assert "%(asctime)s" in called["basic"][1]