'''Performs arthmetic operations using the methods in classes imported in here'''
from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:

    @staticmethod
    def _perform_operation(c: Decimal, d: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(c, d, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(c: Decimal, d: Decimal) -> Decimal:
        return Calculator._perform_operation(c, d, add)
    
    @staticmethod
    def subtract(c: Decimal, d: Decimal) -> Decimal:
        return Calculator._perform_operation(c, d, subtract)
    
    @staticmethod
    def multiply(c: Decimal, d: Decimal) -> Decimal:
        return Calculator._perform_operation(c, d, multiply)
    
    @staticmethod
    def divide(c: Decimal, d: Decimal) -> Decimal:
        return Calculator._perform_operation(c, d, divide)
