import sys
import importlib
import pkgutil
import inspect
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        load_plugins(self.command_handler)

    def start(self):
        while True:
            command_line = input("Enter command: ")
            if command_line.lower() == 'quit':
                print("Goodbye!")
                sys.exit(0)
            self.command_handler.execute_command(command_line)


def load_plugins(handler):
    import app.plugins  # Explicit import of the plugins package
    for _, module_name, _ in pkgutil.iter_modules(app.plugins.__path__):
        full_module_name = f"app.plugins.{module_name}"
        module = importlib.import_module(full_module_name)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                instance = obj()
                handler.register_command(instance.name(), instance)
