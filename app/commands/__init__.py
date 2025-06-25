'''
Class CommandHandler acts as the invoker. It stores commands and knows how to execute them 
based on user input. 
An empty dictionary commands is the constructor method. Maps command names to command objects.
register_command: registers a command with a name.
execute_command: takes a single string from user input to parse, find correct command, 
converts arguments to Decimal, and runs the command.
'''
import logging
from abc import ABC, abstractmethod
from decimal import Decimal

log = logging.getLogger(__name__)

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
        parts = command_line.strip().split()

        if not parts:
            log.warning("No command was entered.")
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
            if result is not None and result != "":
                print(f"Result: {result}")

        except KeyError:
            log.warning(f"Unknown command entered {command_name}.")
            print(f"Unknown command.")
        except Exception as e:
            log.error(f"Error in executing '{command_name}': {e}")
            print(f"Error in executing.")
