from app.commands import Command

class MenuCommand(Command):
    def __inti__(self, handler):
        self.handler = handler

    def name(self):
        return "menu"
    
    def execute(self, *args):
        print("Commands available:")
        for command in sorted(self.handler.commands.keys()):
            print(f"{command}")
