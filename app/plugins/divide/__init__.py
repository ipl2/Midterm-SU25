from app.commands import Command


class DivideCommand(Command):
    def execute(self, *args):
        def name(self):
            return "divide"

        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        
        if args[1] == 0:
            raise ValueError("Cannot divide by zero")
        
        return args[0] / args[1]
