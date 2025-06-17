from decimal import Decimal

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command
    
    def execute_command(self, command_line):
        parts = command_line.strip().split()
        if not parts:
            print("No command was entered.")
            return
        
        command_name = parts[0]
        args = parts [1:]

        command = self.commands.get(command_name)
        if not command:
            print(f"Unkown command: {command_name}")
            return
        
        try:
            decimal_args = [Decimal(arg) for arg in args]
            result = command.execute(*decimal_args)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error in executing {command_name}: {e}")