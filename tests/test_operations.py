from decimal import Decimal
import pytest

from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_add():
    calculated = Calculation(Decimal('4'), Decimal('2'), add)
    assert calculated.perform() == Decimal('6'), "Add failed"

def test_subtract():
    calculated = Calculation(Decimal('4'), Decimal('3'), subtract)
    assert calculated.perform() == Decimal('1'), "Subtract failed"

def test_multiply():
    calculated = Calculation(Decimal('4'), Decimal('2'), multiply)
    assert calculated.perform() == Decimal('8'), "Multiplication failed"

def test_divide():
    calculated = Calculation(Decimal('4'), Decimal('2'), divide)
    assert calculated.perform() == Decimal('2'), "Division failed"

def test_zero_divide():
    with pytest.raises(ValueError, match="Do not divide using zero"):
        calculated = Calculation(Decimal('4'), Decimal('0'), divide)
        calculated.perform()