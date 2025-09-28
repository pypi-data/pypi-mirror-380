"""Libraries"""
import click
from rich.console import Console
from rich.panel import Panel

console = Console()

def success_message(message: str):
    """Creates a success message

    Args:
        message (str): The message you want to send
    """
    new_message = Panel(
        message,
        title="Success!",
        title_align="left",
        border_style="green"
    )
    console.print(new_message)

def error_message(message: str):
    """Creates an error message

    Args:
        message (str): The message you want to send

    Raises:
        click.UsageError: Error handling
    """
    raise click.UsageError(f"Error: {message}")
