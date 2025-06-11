'''Verifying the operations are correct for arithmetic'''
# pylint: disable=unnecessary-dunder-call, invalid-name
import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, divide

def test_calculation_operations(c, d, operation, expected):
    '''Testing is expected returns correctly'''
    calc = Calculation(c, d, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {c} {d}"

def test_calculation_repr():
    '''Testing the correct representation of string'''
    calc = Calculation(Decimal('4'), Decimal('2'), add)
    expected_repr = "Calculation (4, 2, add)"
    assert calc.__repr__() == expected_repr, "The method __repr__ method output is not matching expected string"

def test_division_zero():
    '''Testing the error when dividing by zero'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculation(Decimal('4'), Decimal('0'), divide)
