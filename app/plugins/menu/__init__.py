from app.commands import Command

class MenuCommand(Command):
    def __init__(self, handler):
        self.handler = handler

    def name(self):
        return "menu"
    
    def execute(self, *args):
        commands = [cmd.name() for cmd in self.handler.commands.values()]
        print("Commands available:")
        for cmd_name in commands:
            print(f"- {cmd_name}")
        return ""
