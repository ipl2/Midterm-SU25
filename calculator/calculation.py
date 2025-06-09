'''Class Calculation is found here and referenced in init'''
from decimal import Decimal
from typing import Callable

from calculator.operations import add, subtract, multiply, divide

class Calculation:  
    def __init__(self, c: Decimal, d: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.c = c
        self.d = d
        self.operation = operation
        self.result = self.perform()
    
    def perform(self) -> Decimal:
        return self.operation(self.c, self.d)
    
    @staticmethod
    def create(c: Decimal, d: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        return Calculation(c, d, operation)
