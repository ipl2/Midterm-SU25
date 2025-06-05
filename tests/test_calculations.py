"""Testing if the calculations are correctly performing their intended tasks."""

from decimal import Decimal
import pytest

from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from calculator.calculations import Calculations

@pytest.fixture
def set_calc():
    Calculations.clear()
    Calculations.new_calc(Calculation(Decimal('4'), Decimal('2'), add))
    Calculations.new_calc(Calculation(Decimal('4'), Decimal('2'), subtract))

def test_new_calc(set_calc):
    calculated = Calculation(Decimal('4'), Decimal('2'), add)
    Calculations.new_calc(calculated)
    assert Calculations.latest_calc() == calculated, "Did not add to history"

def test_access_hist(set_calc):
    history = Calculations.access_hist(), "History has incorrect number of calculations"
    assert len(history) == 2

def test_clear(set_calc):
    Calculations.clear()
    assert len(Calculations.access_hist()) == 0, "History not cleared"

def test_latest_calc(set_calc):
    latest = Calculations.latest_calc()
    assert latest.c == Decimal('4') and latest.d == Decimal('2'), "Inccorrect latest calculation"

def test_empty_hist():
    Calculations.clear()
    assert Calculations.latest_calc() is None, "Empty history"