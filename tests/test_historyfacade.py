import pytest
import os
from calculator.history_facade import HistoryFacade

@pytest.fixture(autouse=True)
def reset_singleton():
    HistoryFacade._instance = None

def test_load_from_missing_file(tmp_path):
    fake_path = tmp_path / "does_not_exist.csv"
    hf = HistoryFacade()
    with pytest.raises(FileNotFoundError, match="File is not found."):
        hf.load_from_file(str(fake_path))

def test_delete_existing_file(tmp_path):
    file_path = tmp_path / "test.csv"
    file_path.write_text("operation,operands,result\nadd,1,2")
    hf = HistoryFacade()
    assert os.path.exists(file_path)
    hf.delete_file(str(file_path))
    assert not os.path.exists(file_path)

def test_delete_missing_file(tmp_path):
    file_path = tmp_path / "nope.csv"
    hf = HistoryFacade()
    with pytest.raises(FileNotFoundError, match="File is not found"):
        hf.delete_file(str(file_path))
