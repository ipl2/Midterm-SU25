from app.commands import Command

class MenuCommand(Command):
    def __init__(self, handler):
        self.handler = handler

    def name(self):
        return "menu"
    
    def execute(self, *args):
        print("Commands available:")
        for name in sorted(self.handler.commands):
            print(f"- {name}")
        return ""
