import os
import pandas as pd

class HistoryFacade:
    _instance = None
    COLUMNS = ["operation", "operands", "result"]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.history_df = pd.DataFrame(columns=self.COLUMNS)

    def log_history(self, operation, operands, result):
        entry = {
            "operation": operation,
            "operands": ','.join(map(str, operands)),
            "result": str(result)
        }
        self.history_df = pd.concat(
            [self.history_df, pd.DataFrame([entry])],
            ignore_index=True
        )

    def get_current_history(self):
        return self.history_df.copy()
    
    def clear_history(self):
        self.history_df = pd.DataFrame(columns=self.COLUMNS)

    def save_to_file(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.history_df.to_csv(file_path, index=False)

    def load_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("File is not found.")
        return pd.read_csv(file_path)
    
    def clear_file(self, file_path):
        pd.DataFrame(columns=self.COLUMNS).to_csv(file_path, index=False)

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError("File is not found")
