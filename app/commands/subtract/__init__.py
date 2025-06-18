from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            return args[0] - args[1]
        except IndexError:
            print(f"Two arguments are required.")
        except TypeError:
            print(f"Arguments must be numbers.")
