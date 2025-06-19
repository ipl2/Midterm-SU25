"""Testing the behavior of each command: add, subtract, multiply, & divide"""

from decimal import Decimal
import pytest
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand

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
    command = command_cls()
    result = command.execute(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "command_cls",
    [AddCommand, MultiplyCommand, SubtractCommand, DivideCommand]
)
def test_command_missing_args(command_cls):
    command = command_cls()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(Decimal("5"))  

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))
