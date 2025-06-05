'''How each function must behave'''

from decimal import Decimal

def add(c: Decimal, d: Decimal) -> Decimal:
    return c + d

def subtract(c: Decimal, d: Decimal) -> Decimal:
    return c - d

def multiply(c: Decimal, d: Decimal) -> Decimal:
    return c * d

def divide(c: Decimal, d: Decimal) -> Decimal:
    if d == 0:
        raise ValueError("Do not divide using zero")
    return c / d