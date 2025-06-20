import sys
from app.commands import CommandHandler
from app.plugins import load_plugins


class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        load_plugins(self.command_handler)

        while True:
            command_line = input("Enter command: ")
            if command_line.lower() == 'quit':
                print("Goodbye!")
                sys.exit(0)
            self.command_handler.execute_command(command_line)
