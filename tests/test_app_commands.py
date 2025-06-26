'''Testing the beavior of commands through REPL'''
import pytest
from app import App

def test_app_add_command(monkeypatch, capfd):
    '''tests the REPL add command correctly handles input'''
    inputs = iter(['add 5 5', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        App().start()

    out, _ = capfd.readouterr()
    assert "Result: 10" in out

def test_app_subtract_command(monkeypatch, capfd):
    '''tests the REPL subtract command correctly handles input'''
    inputs = iter(['subtract 10 3', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        App().start()

    out, _ = capfd.readouterr()
    assert "Result: 7" in out

def test_app_multiply_command(monkeypatch, capfd):
    '''tests the REPL multiply command correctly handles input'''
    inputs = iter(['multiply 4 6', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        App().start()

    out, _ = capfd.readouterr()
    assert "Result: 24" in out

def test_app_divide_command(monkeypatch, capfd):
    '''tests the REPL divide command correctly handles input'''
    inputs = iter(['divide 20 4', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        App().start()

    out, _ = capfd.readouterr()
    assert "Result: 5" in out

def test_app_division_by_zero(monkeypatch, capfd):
    '''tests the REPL divide by zero command correctly handles input'''
    inputs = iter(['divide 1 0', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        App().start()

    out, _ = capfd.readouterr()
    assert "Error in executing." in out
