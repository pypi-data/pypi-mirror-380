from typer.testing import CliRunner

from src.cli.calculator import calculator_app
from src.cli.greeter import greeter_app
from src.core import __version__

runner = CliRunner()


def test_add_command():
    result = runner.invoke(calculator_app, ["add", "2", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "The result of addition is: 5.0"


def test_subtract_command():
    result = runner.invoke(calculator_app, ["subtract", "5", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "The result of subtraction is: 2.0"


def test_multiply_command():
    result = runner.invoke(calculator_app, ["multiply", "4", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "The result of multiplication is: 12.0"


def test_divide_command():
    result = runner.invoke(calculator_app, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "The result of division is: 5.0"


def test_version_flag():
    result = runner.invoke(calculator_app, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == f"python-template v{__version__}"


def test_greeter():
    result = runner.invoke(greeter_app, ["greet"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, world!"

    result = runner.invoke(greeter_app, ["greet", "Johnny"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Johnny!"
