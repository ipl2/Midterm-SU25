import importlib
import pkgutil
import inspect
from app.commands import Command

def load_plugins(handler):
    package = __name__
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        full_module_name = f"{package}.{module_name}"
        module = importlib.import_module(full_module_name)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                instance = obj()
                handler.register_command(instance.name(), instance)
