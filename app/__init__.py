import sys
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands import CommandHandler


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command('add', AddCommand())
        self.command_handler.register_command('subtract', SubtractCommand())
        self.command_handler.register_command('multiply', MultiplyCommand())
        self.command_handler.register_command('divide', DivideCommand())

        while True:
            command_line = input("Enter command: ")
            if command_line.lower() == 'quit':
                print("Goodbye!")
                sys.exit(0)
            self.command_handler.execute_command(command_line)
