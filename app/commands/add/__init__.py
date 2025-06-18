from app.commands import Command
from decimal import Decimal

class AddCommand(Command):
    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        try:
            return args[0] + args[1]
        except TypeError:
            raise ValueError("Arguments must be numbers.")
