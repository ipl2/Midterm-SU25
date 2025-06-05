'''Testing the class Calculator found in the innit file'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(3,3) == 6

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(3,3) == 0

def test_multiply():
    '''Test that multiplication function works'''
    assert Calculator.multiply(3,3) == 9

def test_divide():
    '''Test that division function works'''
    assert Calculator.divide(3,3) == 1
