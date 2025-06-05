from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculations] = []

    @classmethods
    def new_calc(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def access_hist(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def latest_calc(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]  #get the last digit in list
        return None
    
    @classmethod
    def clear(cls):
        cls.history.clear()
