import pandas as pd

class HistoryFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.history_df = pd.DataFrame(columns=["operation", "operands", "result"])

    def log_history(self, operation, operands, result):
        new_entry = {"operation": operation, "operands": ','.join(map(str, operands)), "result": str(result)}
        self.history_df = pd.concat([self.history_df, pd.DataFrame([new_entry])], ignore_index=True)

    def get_current_history(self):
        return self.history_df.copy()
    
    def clear_history(self):
        self.history_df = pd.DataFrame(columns=["operation", "operands", "result"])
