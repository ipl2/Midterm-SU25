import inspect
from app.commands import CommandHandler, Command

class CommandFactory:
    def __init__(self, handler: CommandHandler):
        self.handler = handler

    def create(self, command_class: type[Command]) -> Command:
        sig = inspect.signature(command_class)
        parameters = sig.parameters

        if len(parameters) == 1 and 'handler' in parameters:
            return command_class(self.handler)
        return command_class()
