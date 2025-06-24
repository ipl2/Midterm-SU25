import logging
from app.commands import Command
from decimal import Decimal, InvalidOperation

log = logging.getLogger(__name__)

class MultiplyCommand(Command):
    def name(self):
        return "multiply"

    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")

        try:
            c = Decimal(str(args[0]))
            d = Decimal(str(args[1]))
        except InvalidOperation:
            raise ValueError("Invalid decimal input.")

        result = c * d
        log.info(f"Result: {result}")
        return result
