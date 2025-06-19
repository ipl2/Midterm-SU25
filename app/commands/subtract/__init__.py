from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")

        return args[0] - args[1]
