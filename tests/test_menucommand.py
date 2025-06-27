'''Testing functionality of MenuCommand'''

from app.plugins.menu import MenuCommand

class DummyHandler:
    '''dict of commands mapped to none to simulate a command handler'''
    def __init__(self):
        self.commands = {
            "add": None,
            "subtract": None,
            "multiply": None,
            "divide": None,
        }

def test_menucommand_name():
    '''tests the command returns menu'''
    handler = DummyHandler()
    cmd = MenuCommand(handler)
    assert cmd.name() == "menu"

def test_menucommand_execute(capsys):
    '''tests that command prints and returns empty string'''
    handler = DummyHandler()
    cmd = MenuCommand(handler)
    result = cmd.execute()

    captured = capsys.readouterr().out
    assert "Commands available:" in captured
    for command_name in handler.commands:
        assert f"- {command_name}" in captured
    assert result == ""
