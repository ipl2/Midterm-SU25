import pytest
from calculator.history_facade import HistoryFacade
from app.plugins.csv import SaveHistoryCommand, LoadHistoryCommand, ClearHistoryCommand, DeleteHistoryCommand

def test_save_history():
    '''tests the save command saves history'''
    history = HistoryFacade()
    history.log_history("add", [1, 2], 3)
    command = SaveHistoryCommand()
    result = command.execute()
    assert result == "History saved."

def test_load_history(capsys):
    '''tests the load command loads history'''
    command = LoadHistoryCommand()
    result = command.execute()
    output = capsys.readouterr().out
    assert "add" in output or "History file is empty." in result

def test_clear_history():
    '''tests the clear command clears history'''
    command = ClearHistoryCommand()
    result = command.execute()
    assert result == "History is cleared."

def test_delete_history():
    '''tests the delete command deletes history'''
    command = DeleteHistoryCommand()
    result = command.execute()
    assert result in ["History is deleted.", "No history file."]
