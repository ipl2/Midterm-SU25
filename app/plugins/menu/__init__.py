from app.commands import Command

class MenuCommand(Command):
    def name(self):
        return "menu"
    
    def execute(self, *args):
        print("Available commands:")
        from app.commands import registered_commands
        for command_name in sorted(registered_commands()):
            print(f"{command_name}")