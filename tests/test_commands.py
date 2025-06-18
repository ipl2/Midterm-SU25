import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand

def test_add_command(capfd):
    command = AddCommand()
    result = command.execute(Decimal("4"), Decimal("2"))
    assert result == Decimal("6")

def test_multiply_command(capfd):
    command = MultiplyCommand()
    result = command.execute(Decimal("4"), Decimal("2"))
    assert result == Decimal("8")

def test_subtract_command(capfd):
    command = SubtractCommand()
    result = command.execute(Decimal("2"), Decimal("2"))
    assert result == Decimal("0")

def test_divide_command(capfd):
    command = DivideCommand()
    result = command.execute(Decimal("2"), Decimal("2"))
    assert result == Decimal("1")

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))
