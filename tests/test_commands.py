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
    command = command_class()
    with pytest.raises(ValueError, match=error_msg):
        command.execute(*args)

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))

'''def test_add_command(capfd):
    command = AddCommand()
    result = command.execute(Decimal("4"), Decimal("2"))
    assert result == Decimal("6")

def test_add_command_missing_args():
    command = AddCommand()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(1)

def test_add_command_invalid_types():
    command = AddCommand()
    with pytest.raises(ValueError, match="Arguments must be numbers."):
        command.execute(1, "a")



def test_multiply_command(capfd):
    command = MultiplyCommand()
    result = command.execute(Decimal("4"), Decimal("2"))
    assert result == Decimal("8")

def test_multiply_command_missing_args():
    command = MultiplyCommand()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(Decimal("5"))

def test_multiply_command_invalid_types():
    command = MultiplyCommand()
    with pytest.raises(ValueError, match="Arguments must be numbers."):
        command.execute("a", "b")



def test_subtract_command(capfd):
    command = SubtractCommand()
    result = command.execute(Decimal("2"), Decimal("2"))
    assert result == Decimal("0")

def test_subtract_command_missing_args():
    command = SubtractCommand()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(Decimal("5"))

def test_subtract_command_invalid_types():
    command = SubtractCommand()
    with pytest.raises(ValueError, match="Arguments must be numbers."):
        command.execute("a", "b")



def test_divide_command(capfd):
    command = DivideCommand()
    result = command.execute(Decimal("2"), Decimal("2"))
    assert result == Decimal("1")

def test_divide_command_missing_args():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Two arguments are required."):
        command.execute(1)

def test_divide_command_invalid_types():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Arguments must be numbers."):
        command.execute("a", "b")

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal("1"), Decimal("0"))'''
