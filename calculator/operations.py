'''How each function must behave'''

def add(c,d):
    return c + d

def subtract(c,d):
    return c - d

def multiply(c,d):
    return c * d

def divide(c,d):
    try:
        return c/d
    except ZeroDivisionError:
        None