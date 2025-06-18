from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            return args[0] / args[1]
        except IndexError:
            print(f"Two arguments are required.")
        except TypeError:
            print(f"Arguments must be numbers.")
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
