
# pylint: disable=invalid-name
"""Testing the behavior of each command: add, subtract, multiply, & divide"""
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
    '''tests commands are executing expected results'''
    command = command_cls()
    result = command.execute(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "command_cls",
    [AddCommand, MultiplyCommand, SubtractCommand, DivideCommand]
)
def test_command_missing_args(command_cls):
    '''tests missing arguments returns the raised ValueError'''
    command = command_cls()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(Decimal("5"))
def test_divide_by_zero():
    '''tests division by zero error raises ValueError'''
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))

@pytest.mark.parametrize("command_cls", [AddCommand, SubtractCommand, MultiplyCommand, DivideCommand])
def test_invalid_decimal_input(command_cls):
    '''tests invalid input and raises correct error'''
    command = command_cls()
    with pytest.raises(ValueError, match="Invalid decimal input."):
        command.execute("Invalid", "2")
