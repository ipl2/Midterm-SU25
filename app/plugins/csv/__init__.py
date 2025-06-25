import logging
import os
import pandas as pd
from app.commands import Command
from calculator.history_facade import HistoryFacade

DATA_DIR = os.getenv("DATA_DIR", "data")
HISTORY_FILE = os.getenv("HISTORY_FILE", "calculator_history.csv")
FILE_PATH = os.path.join(DATA_DIR, HISTORY_FILE)

logger = logging.getLogger(__name__)

class SaveHistoryCommand(Command):
    def name(self):
        return "save_history"
    
    def execute(self, *args):
        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            HistoryFacade().save_to_file(FILE_PATH)
            logger.info(f"History is saved to this path: {FILE_PATH}")
            return "History saved."
        except Exception as e:
            logger.error(f"Failed to save to history: {e}")
            return "Error in saving to history"
        
class LoadHistoryCommand(Command):
    def name(self):
        return "load_history"
    
    def execute(self, *args):
        try:
            df = HistoryFacade().load_from_file(FILE_PATH)
            if df.empty:
                return "History file is empty."
            print(df.to_string(index=False))
            logger.info("History is loaded.")
            return ""
        except FileNotFoundError:
            return "History file is not found."
        except Exception as e:
            logger.error(f"Failed to load the history: {e}")
            return "Error in loading history."
        
class ClearHistoryCommand(Command):
    def name(self):
        return "clear_history"
    
    def execute(self, *args):
        try:
            facade = HistoryFacade()
            facade.clear_history()
            facade.clear_file(FILE_PATH)
            logger.info("History is all cleared from file.")
            return "History is cleared."
        except Exception as e:
            logger.error(f"Failed to clear all history: {e}")
            return "Error in clearing the history."

class DeleteHistoryCommand(Command):
    def name(self):
        return "delete_history"
    
    def execute(self, *args):
        try:
            HistoryFacade().delete_file(FILE_PATH)
            logger.info("History file no longer exists from deletion.")
            return "History is deleted."
        except FileNotFoundError:    
            return "No history file."
        except Exception as e:
            logger.error(f"Failure in deleting history: {e}")
            return "Error deleting the history."
