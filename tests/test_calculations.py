"""Testing if the calculations are correctly performing their intended tasks."""

from decimal import Decimal
import pytest

from calculator.operations import add, subtract
from calculator.calculation import Calculation
from calculator.calculations import Calculations

@pytest.fixture
def setup_calculations():
    '''Fixture to reset history calculation and add two other'''
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('4'), Decimal('2'), add))
    Calculations.add_calculation(Calculation(Decimal('4'), Decimal('2'), subtract))

def test_add_calculation(setup_calculations):
    '''Testing if new calculation is added to history'''
    calc = Calculation(Decimal('4'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Did not add to history"

def test_get_history(setup_calculations):
    '''testing if history is accessible'''
    history = Calculations.get_history()
    assert len(history) == 2, "History has incorrect number of calculations"

def test_clear_history(setup_calculations):
    '''Testing if history clears'''
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History not cleared"

def test_get_latest(setup_calculations):
    '''Testing the lastest expected calculation'''
    latest = Calculations.get_latest()
    assert latest.c == Decimal('4') and latest.d == Decimal('2'), "Incorrect latest calculation"

def test_find_by_operation(setup_calculations):
    '''Testing calculations matches specific operation'''
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations performed with add"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations performed with subtract"

def test_get_latest_with_empty_history():
    '''Testing to see if it checks when history is empty'''
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Empty history"
