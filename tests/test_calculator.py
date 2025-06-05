'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(3,3) == 6

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(3,3) == 0

def test_multiply():
    '''Test that multiplication function works'''
    assert multiply(3,3) == 9

def test_divide():
    '''Test that division function works'''
    assert divide(3,3) == 1
