'''Testing the behavior of each command: add, subtract, multiply, & divide'''

from decimal import Decimal
import pytest
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand

@pytest.mark.parametrize("command_class, args, expected", [
    (AddCommand, (Decimal("4"), Decimal("2")), Decimal("6")),
    (MultiplyCommand, (Decimal("4"), Decimal("2")), Decimal("8")),
    (SubtractCommand, (Decimal("2"), Decimal("2")), Decimal("0")),
    (DivideCommand, (Decimal("2"), Decimal("2")), Decimal("1")),
])
def test_command_execute_success(command_class, args, expected):
    '''test execution of command classes: add, subtract, multiply, divide to ensure it returns
    correct result'''
    command = command_class()
    result = command.execute(*args)
    assert result == expected

@pytest.mark.parametrize("command_class, args, error_msg", [
    (AddCommand, (1,), "Two arguments are required."),
    (AddCommand, (1, "a"), "Arguments must be numbers."),
    (MultiplyCommand, (Decimal("5"),), "Two arguments are required."),
    (MultiplyCommand, ("a", "b"), "Arguments must be numbers."),
    (SubtractCommand, (Decimal("5"),), "Two arguments are required."),
    (SubtractCommand, ("a", "b"), "Arguments must be numbers."),
    (DivideCommand, (1,), "Two arguments are required."),
    (DivideCommand, ("a", "b"), "Arguments must be numbers."),
])
def test_command_execute_value_errors(command_class, args, error_msg):
    '''tests ValueError is raised for invalid arguments (missing arguments & non-numeric)'''
    command = command_class()
    with pytest.raises(ValueError, match=error_msg):
        command.execute(*args)

def test_divide_by_zero():
    '''testing divide by zero is raising a ValueError'''
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))
