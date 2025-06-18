import pytest
from app.commands import Command
from app.commands import CommandHandler

def test_command_is_abstract():
    with pytest.raises(TypeError):
        Command()

def test_command_handler_no_input(capfd):
    handler = CommandHandler()
    handler.execute_command("")
    out, _ = capfd.readouterr()
    assert "No command was entered." in out

def test_command_handler_invalid_decimal(capfd):
    class DummyCommand:
        def execute(self, *args):
            return sum(args)

    handler = CommandHandler()
    handler.register_command("dummy", DummyCommand())
    handler.execute_command("dummy a b")
    out, _ = capfd.readouterr()
    assert "Error in executing dummy" in out
