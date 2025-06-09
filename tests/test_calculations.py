"""Testing if the calculations are correctly performing their intended tasks."""

from decimal import Decimal
import pytest

from calculator.operations import add, subtract
from calculator.calculation import Calculation
from calculator.calculations import Calculations

@pytest.fixture
def set_calc():
    '''Fixture to reset history calculation and add two other'''
    Calculations.clear()
    Calculations.new_calc(Calculation(Decimal('4'), Decimal('2'), add))
    Calculations.new_calc(Calculation(Decimal('4'), Decimal('2'), subtract))

def test_new_calc(set_calc):
    '''Testing if new calculation is added to history'''
    calculated = Calculation(Decimal('4'), Decimal('2'), add)
    Calculations.new_calc(calculated)
    assert Calculations.latest_calc() == calculated, "Did not add to history"

def test_access_hist(set_calc):
    '''testing if history is accessible'''
    history = Calculations.access_hist()
    assert len(history) == 2, "History has incorrect number of calculations"

def test_clear(set_calc):
    '''Testing if history clears'''
    Calculations.clear()
    assert len(Calculations.access_hist()) == 0, "History not cleared"

def test_latest_calc(set_calc):
    '''Testing the lastest expected calculation'''
    latest = Calculations.latest_calc()
    assert latest.c == Decimal('4') and latest.d == Decimal('2'), "Incorrect latest calculation"

def test_find_operation(set_calc):
    '''Testing calculations matches specific operation'''
    add_operations = Calculations.find_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations performed with add"
    subtract_operations = Calculations.find_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations performed with subtract"

def test_empty_hist():
    '''Testing to see if it checks when history is empty'''
    Calculations.clear()
    assert Calculations.latest_calc() is None, "Empty history"
