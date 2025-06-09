'''Testing the calculator operaration using the Calculations class'''

from decimal import Decimal
import pytest

from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_operation_add():
    '''Testing addition function'''
    calculation = Calculation(Decimal('4'), Decimal('2'), add)
    assert calculation.perform() == Decimal('6'), "Add failed"

def test_operation_subtract():
    '''Testing subtraction function'''
    calculation = Calculation(Decimal('4'), Decimal('3'), subtract)
    assert calculation.perform() == Decimal('1'), "Subtract failed"

def test_operation_multiply():
    '''Testing multiplication function'''
    calculation = Calculation(Decimal('4'), Decimal('2'), multiply)
    assert calculation.perform() == Decimal('8'), "Multiplication failed"

def test_operation_divide():
    '''Testing division function'''
    calculation = Calculation(Decimal('4'), Decimal('2'), divide)
    assert calculation.perform() == Decimal('2'), "Division failed"

def test_divide_by_zero():
    '''Testing division by zero function and error'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculation(Decimal('4'), Decimal('0'), divide)
