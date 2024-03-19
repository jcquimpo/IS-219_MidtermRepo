'''test_commands.py'''

import pytest
from app import App
# from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected" 
        
def test_add_command(capfd, monkeypatch):
    """Test the execution of the AddCommand."""
    inputs = iter(['5 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = AddCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "The sum of 5.0 and 7.0 is: 12.0"

def test_add_command_invalid_input(capfd, monkeypatch):
    """Test the execution of the AddCommand with invalid input."""
    inputs = iter(['abc def'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = AddCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "Please enter valid numbers."
    
    
def test_subtract_command(capfd, monkeypatch):
    """Test the execution of the SubtractCommand."""
    inputs = iter(['7 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = SubtractCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "The difference of 7.0 and 7.0 is: 0.0"

def test_subtract_command_invalid_input(capfd, monkeypatch):
    """Test the execution of the SubtractCommand with invalid input."""
    inputs = iter(['abc def'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = SubtractCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "Please enter valid numbers."
    
def test_multiply_command(capfd, monkeypatch):
    """Test the execution of the MultiplyCommand."""
    inputs = iter(['5 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = MultiplyCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "The product of 5.0 and 7.0 is: 35.0"

def test_multiply_command_invalid_input(capfd, monkeypatch):
    """Test the execution of the MultiplyCommand with invalid input."""
    inputs = iter(['abc def'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = MultiplyCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "Please enter valid numbers."
    
def test_divide_command(capfd, monkeypatch):
    """Test the execution of the DivideCommand."""
    inputs = iter(['7 7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = DivideCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "The quotient of 7.0 and 7.0 is: 1.0"

def test_divide_command_invalid_input(capfd, monkeypatch):
    """Test the execution of the DivideCommand with invalid input."""
    inputs = iter(['abc def'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = DivideCommand()
    command.execute()

    out, _ = capfd.readouterr()
    assert out.strip() == "Please enter valid numbers."    