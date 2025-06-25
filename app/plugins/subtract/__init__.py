import logging
from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.history_facade import HistoryFacade

log = logging.getLogger(__name__)

class SubtractCommand(Command):
    def name(self):
        return "subtract"

    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")

        try:
            c = Decimal(str(args[0]))
            d = Decimal(str(args[1]))
        except InvalidOperation:
            raise ValueError("Invalid decimal input.")

        result = c - d
        HistoryFacade().log_history("subtract", [c, d], result)
        return result
