'''Testing the calculator operaration using the Calculations class'''

from decimal import Decimal
import pytest

from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_op_add():
    '''Testing addition function'''
    calculated = Calculation(Decimal('4'), Decimal('2'), add)
    assert calculated.perform() == Decimal('6'), "Add failed"

def test_op_subtract():
    '''Testing subtraction function'''
    calculated = Calculation(Decimal('4'), Decimal('3'), subtract)
    assert calculated.perform() == Decimal('1'), "Subtract failed"

def test_op_multiply():
    '''Testing multiplication function'''
    calculated = Calculation(Decimal('4'), Decimal('2'), multiply)
    assert calculated.perform() == Decimal('8'), "Multiplication failed"

def test_op_divide():
    '''Testing division function'''
    calculated = Calculation(Decimal('4'), Decimal('2'), divide)
    assert calculated.perform() == Decimal('2'), "Division failed"

def test_zero_op_divide():
    '''Testing division by zero function and error'''
    with pytest.raises(ValueError, match="Do not divide using zero"):
        Calculation(Decimal('4'), Decimal('0'), divide)
