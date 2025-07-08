'''testing the commands of history functionality and their commands'''

from unittest.mock import patch, MagicMock
import pytest
from calculator.history_facade import HistoryFacade
from app.plugins.csv import SaveHistoryCommand, LoadHistoryCommand, ClearHistoryCommand, DeleteHistoryCommand

@pytest.fixture
def mock_facade():
    '''patches HistoryFacade to avoid real file system operations'''
    with patch("app.plugins.csv.HistoryFacade") as mock:
        yield mock

@pytest.fixture
def command_instances():
    '''fixture creates instances of all command classes'''
    return {
        "save": SaveHistoryCommand(),
        "load": LoadHistoryCommand(),
        "clear": ClearHistoryCommand(),
        "delete": DeleteHistoryCommand()
    }

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

def test_save_history_failure(mock_facade, command_instances):
    '''tests command SaveHistoryCommand behavior'''
    mock_facade.return_value.save_to_file.side_effect = Exception("Save failed")
    result = command_instances["save"].execute()
    assert result == "Error in saving to history"

def test_load_history_file_not_found(mock_facade, command_instances):
    '''tests command LoadHistoryCommand behavior when file is missing'''
    mock_facade.return_value.load_from_file.side_effect = FileNotFoundError()
    result = command_instances["load"].execute()
    assert result == "History file is not found."

def test_load_history_failure(mock_facade, command_instances):
    '''tests command LoadHistoryCommand behavior when load fails'''
    mock_facade.return_value.load_from_file.side_effect = Exception("Load failed")
    result = command_instances["load"].execute()
    assert result == "Error in loading history."

def test_load_history_empty(mock_facade, command_instances):
    '''tests command LoadHistoryCommand behavior when DataFrame is empty'''
    mock_df = MagicMock()
    mock_df.empty = True
    mock_facade.return_value.load_from_file.return_value = mock_df
    result = command_instances["load"].execute()
    assert result == "History file is empty."

def test_clear_history_failure(mock_facade, command_instances):
    '''tests command ClearHistoryCommand behavior'''
    mock_facade.return_value.clear_file.side_effect = Exception("Clear failed")
    result = command_instances["clear"].execute()
    assert result == "Error in clearing the history."

def test_delete_history_file_not_found(mock_facade, command_instances):
    '''tests command DeleteHistoryCommand behavior when file is not found'''
    mock_facade.return_value.delete_file.side_effect = FileNotFoundError()
    result = command_instances["delete"].execute()
    assert result == "No history file."

def test_delete_history_failure(mock_facade, command_instances):
    '''tests command DeleteHistoryCommand behavior'''
    mock_facade.return_value.delete_file.side_effect = Exception("Delete failed")
    result = command_instances["delete"].execute()
    assert result == "Error deleting the history."
