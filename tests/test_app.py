'''Testing the behavior of App class.'''

import pytest
from app import App


# add a test environment variable

def test_app_start_quit_command(capfd, monkeypatch):
    '''tests function when user types exit'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    out = capfd.readouterr().out
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    '''tests function when user types a unrecognized command'''
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    out = capfd.readouterr().out
    assert "Unknown command." in out
