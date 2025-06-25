import logging
from app.commands import Command

logger = logging.getLogger(__name__)

class CommandFactory:
    _registry = {}

    @classmethod
    def register_command(cls, name, command_class):
        if not issubclass(command_class, Command):
            raise TypeError(f"{command_class.__name__} must be inheritted from Command.")
        cls._registry[name.lower()] = command_class
        logger.info(f"Command is Registered: {name.lower()}")

    @classmethod
    def create_command(cls, name, handler=None):
        command_class = cls._registry.get(name.lower())
        if not command_class:
            raise ValueError(f"Unknown registered name: {name}")
        try:
            return command_class(handler) if handler else command_class()
        except TypeError as e:
            logger.warning(f"Could not instantiate: {e}")
            return command_class()
