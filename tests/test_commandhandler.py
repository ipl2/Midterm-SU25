import pytest
from app.commands import Command, CommandHandler

def test_command_is_abstract():
    with pytest.raises(TypeError):
        Command()

def test_command_handler_no_input(capsys):
    handler = CommandHandler()
    handler.execute_command("")
    captured = capsys.readouterr()
    assert "No command was entered." in captured.out

def test_execute_command_non_string_input(capsys):
    handler = CommandHandler()
    handler.execute_command(123)  # passing int instead of str
    captured = capsys.readouterr()
    assert "Command must be a string." in captured.out

def test_command_handler_single_newline(capsys):
    handler = CommandHandler()
    handler.execute_command("\n")
    captured = capsys.readouterr()
    assert "No command was entered." in captured.out

def test_command_handler_invalid_decimal(capsys):
    class DummyCommand:
        def execute(self, *args):
            return sum(args)
    handler = CommandHandler()
    handler.register_command("dummy", DummyCommand())
    handler.execute_command("dummy a b")
    captured = capsys.readouterr()
    assert "Error in executing dummy" in captured.out

def test_command_handler_unknown_command(capsys):
    handler = CommandHandler()
    handler.execute_command("unknowncmd 1 2")
    captured = capsys.readouterr()
    assert "Unknown command: unknowncmd" in captured.out

def test_command_handler_valid_execution(capsys):
    class AddCommand(Command):
        def execute(self, *args):
            return sum(args)
    handler = CommandHandler()
    handler.register_command("add", AddCommand())
    handler.execute_command("add 1 2 3")
    captured = capsys.readouterr()
    assert "Result: 6" in captured.out
