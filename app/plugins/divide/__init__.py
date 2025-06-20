from app.commands import Command


class DivideCommand(Command):
    def name(self):
        return "divide"

    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        
        if args[1] == 0:
            raise ValueError("Cannot divide by zero")
        
        return args[0] / args[1]
