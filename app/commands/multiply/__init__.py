from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            return args[0] * args[1]
        except IndexError:
            raise ValueError("Two arguments are required.")
        except TypeError:
            raise ValueError("Arguments must be numbers.")
