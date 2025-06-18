from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            return args[0] / args[1]
        except IndexError:
            raise ValueError("Two arguments are required.")
        except TypeError:
            raise ValueError("Arguments must be numbers.")
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
