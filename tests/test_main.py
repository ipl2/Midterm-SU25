'''Has parametrize to check for specific tests'''
import pytest
import sys
from main import calculate_and_print, main
from calculator.operations import divide

@pytest.mark.parametrize("c_string, d_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(c_string, d_string, operation_string, expected_string, capsys):
    '''Testing ouputs to print the correct result given the string inputs (add, subtract ...)
    and operation (+, - ...)'''
    calculate_and_print(c_string, d_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_main_valid(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "2", "3", "add"])
    main()
    captured = capsys.readouterr()
    assert "The result of 2 add 3 is equal to 5" in captured.out

def test_main_usage_and_exit(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "2", "add"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Usage: python calculator_main.py <number1> <number2> <operation>" in captured.out

def test_main_zero_division(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "1", "0", "divide"])
    main()
    captured = capsys.readouterr()
    assert "An error occurred: Cannot divide by zero" in captured.out
