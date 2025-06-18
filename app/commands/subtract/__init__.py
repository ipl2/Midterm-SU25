from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            return args[0] - args[1]
        except (IndexError, TypeError):
            raise ValueError("Two arguments are required.")
