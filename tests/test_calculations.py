"""Testing if the calculations are correctly performing their intended tasks."""

from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test if addition works'''
    assert add(3, 3) == 6

def test_subtract():
    '''Test if subtraction works'''
    assert subtract(3, 3) == 0

def test_multiply():
    '''Test if multiplication works'''
    assert multiply(3, 3) == 9

def test_division():
    '''Test if division works'''
    assert divide(3, 3) == 1
