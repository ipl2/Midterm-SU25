import logging
from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.history_facade import HistoryFacade

class DivideCommand(Command):
    def name(self):
        return "divide"

    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        
        try:
            c = Decimal(str(args[0]))
            d = Decimal(str(args[1]))
        except InvalidOperation:
            raise ValueError("Invalid decimal input.")
        
        if d == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = c / d
        HistoryFacade().log_history("divide", [c, d], result)
        return result
