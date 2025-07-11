import sys
import os
import logging
import logging.config
import importlib
import pkgutil
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.factory import CommandFactory

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.command_factory = CommandFactory(self.command_handler)

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        try:
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        except Exception:
            logging.basicConfig(level =logging.INFO, format='%(asctime)s - %(levelname)s- %(message)s')
        logging.info("Logging is configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environmet variables is loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        try:
            import app.plugins
        except ImportError as e:
            logging.error(f"Import plugin package failed: {e}")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules(app.plugins.__path__):
            if is_pkg:
                try:
                    full_module_name = f"{plugins_package}.{plugin_name}"
                    plugin_module = importlib.import_module(full_module_name)
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Importing plugin '{plugin_name}' failed: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                try:
                    instance = self.command_factory.create(item)
                except TypeError:
                    instance = item()
                command_name = instance.name() if hasattr(instance, 'name') else plugin_name
                self.command_handler.register_command(command_name, instance)
                logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Exit command received.")
                    sys.exit(0)
                try:
                    result = self.command_handler.execute_command(cmd_input)
                    if result:
                        print(result)
                except KeyError:
                    logging.warning(f"Unknown command entered: '{cmd_input}'")
                except Exception as e:
                    logging.error(f"Error executing command '{cmd_input}': {e}", exc_info=True)
        except KeyboardInterrupt:
            logging.info("KeyboardInterrupt: exiting gracefully.")
        finally:
            logging.info("Application shutdown.")
            sys.exit(0)

if __name__ == "__main__":
    App().start()
