'''
Class CommandHandler acts as the invoker. It stores commands and knows how to execute them 
based on user input. 
An empty dictionary commands is the constructor method. Maps command names to command objects.
register_command: registers a command with a name.
execute_command: takes a single string from user input to parse, find correct command, 
converts arguments to Decimal, and runs the command.
'''
from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass # pragma: no cover

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name.lower()] = command
    
    def execute_command(self, command_line):
        try:
            parts = command_line.strip().split()
        except AttributeError:
            print("Command must be a string.")
            return

        if not parts:
            print("No command was entered.")
            return

        command_name = parts[0].lower()
        args = parts[1:]

        try:
            command = self.commands[command_name] 
            try:
                parsed_args = [Decimal(arg) for arg in args]
            except Exception:
                parsed_args = args

            result = command.execute(*parsed_args)
            if result is not None:
                print(f"Result: {result}")

        except KeyError:
            print(f"Unknown command: {command_name}")
        except Exception as e:
            print(f"Error in executing '{command_name}': {e}")





        '''try:
            command = self.commands[command_name]
            decimal_args = [Decimal(arg) for arg in args]
            result = command.execute(*decimal_args)
            print(f"Result: {result}")
        except KeyError:
            print(f"Unknown command: {command_name}")
        except Exception as e:
            print(f"Error in executing {command_name}: {e}")'''
