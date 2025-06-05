'''Verifying the operations are correct for arithmetic'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("c, d, operation, expected", [
    (Decimal('4'), Decimal('2'), add, Decimal('6')),
    (Decimal('4'), Decimal('2'), subtract, Decimal('2')),
    (Decimal('4'), Decimal('2'), multiply, Decimal('8')),
    (Decimal('4'), Decimal('4'), divide, Decimal('1')),

    (Decimal('4.6'), Decimal('2'), add, Decimal('6.6')),
    (Decimal('4.6'), Decimal('2'), subtract, Decimal('2.6')),
    (Decimal('4.6'), Decimal('2'), multiply, Decimal('9.2')),
    (Decimal('4.6'), Decimal('2'), divide, Decimal('2.3')),
])

def test_calculation_op(c, d, operation, expected):
    calculated = Calculation(c, d, operation)
    assert calculated.perform() == expected

def test_division_zero():
    with pytest.raises(ValueError, match="Do not divide using zero"):
        calculation = Calculation(Decimal('4'), Decimal('0'), divide)
