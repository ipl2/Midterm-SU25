'''Testing the calculator operaration using the Calculations class'''
import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operations(c, d, operation, expected):
    '''Knows to get parameter out of conftest.py modified_parameters to make
    sure Calculation class is all good'''
    calculation = Calculation.create(c, d, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Making sure the division by zero is functioning correctly'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('4'), Decimal('0'), divide)
        calculation.perform()
