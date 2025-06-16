from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]  #get the last digit in list
        return None
    
    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]