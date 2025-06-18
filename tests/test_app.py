import pytest
from app import App

def test_app_start_quit_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()
    
    out, err = capfd.readouterr()
    assert "Goodbye!" in out
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    inputs = iter(['unknown_command', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "Unknown command: unknown_command" in out
    assert "Goodbye" in out
