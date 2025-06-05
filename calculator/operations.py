from decimal import Decimal

'''How each function must behave'''

def add(c: Decimal, d: Decimal) -> Decimal:
    return c + d

def add(c: Decimal, d: Decimal) -> Decimal:
    return c - d

def add(c: Decimal, d: Decimal) -> Decimal:
    return c * d

def add(c: Decimal, d: Decimal) -> Decimal:
    if d == 0:
        raise ZeroDivisionError("Do not divide using zero")
    return a / b