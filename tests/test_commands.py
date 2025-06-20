import pytest
from app import App

def test_app_add_command(monkeypatch, capfd):
    inputs = iter(['add 5 5', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    out, _ = capfd.readouterr()
    assert "Result: 10" in out
    assert "Goodbye!" in out

def test_app_subtract_command(monkeypatch, capfd):
    inputs = iter(['subtract 10 3', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    out, _ = capfd.readouterr()
    assert "Result: 7" in out
    assert "Goodbye!" in out

def test_app_multiply_command(monkeypatch, capfd):
    inputs = iter(['multiply 4 6', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    out, _ = capfd.readouterr()
    assert "Result: 24" in out
    assert "Goodbye!" in out

def test_app_divide_command(monkeypatch, capfd):
    inputs = iter(['divide 20 4', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    out, _ = capfd.readouterr()
    assert "Result: 5" in out
    assert "Goodbye!" in out








'''# pylint: disable=invalid-name

# Testing the behavior of each command: add, subtract, multiply, & divide

from decimal import Decimal
import pytest
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand

@pytest.mark.parametrize(
    "command_cls, a, b, expected",
    [
        (AddCommand, Decimal("4"), Decimal("2"), Decimal("6")),
        (MultiplyCommand, Decimal("4"), Decimal("2"), Decimal("8")),
        (SubtractCommand, Decimal("2"), Decimal("2"), Decimal("0")),
        (DivideCommand, Decimal("2"), Decimal("2"), Decimal("1")),
    ]
)
def test_command_execute(command_cls, a, b, expected):
    # tests commands are executing expected results
    command = command_cls()
    result = command.execute(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "command_cls",
    [AddCommand, MultiplyCommand, SubtractCommand, DivideCommand]
)
def test_command_missing_args(command_cls):
    # tests missing arguments returns the raised ValueError
    command = command_cls()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(Decimal("5"))

def test_divide_by_zero():
    # tests division by zero error raises ValueError
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))'''
