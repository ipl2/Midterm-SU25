from app.commands import Command

class MenuCommand(Command):
    def __init__(self, handler):
        self.handler = handler

    def name(self):
        return "menu"
    
    def execute(self, *args):
        commands = sorted(self.handler.commands.keys())
        print("Commands available:")
        for cmd in commands:
            print(f"- {cmd}")
            return None
