"""
This module provides CLI commands for greeting people.

The module relies on the `core.greeter` module for the actual greeting logic.
"""

from typing import Annotated, Optional

import typer

from src import core
from src.core import greeter

greeter_app = typer.Typer()


@greeter_app.command()
def greet(
    name: Annotated[
        str,
        typer.Argument(help="The name of the person to greet."),
    ] = "",
) -> None:
    """
    Greet someone.

    Args:
        name: The name of the person to greet. If name is omitted, the world
            will be greeted.
    """
    greeting = greeter.greeting(name)
    typer.echo(greeting)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{core.__app_name__} v{core.__version__}")
        raise typer.Exit()


@greeter_app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    """Handles the --version flag"""
    return


if __name__ == "__main__":
    greeter_app()
