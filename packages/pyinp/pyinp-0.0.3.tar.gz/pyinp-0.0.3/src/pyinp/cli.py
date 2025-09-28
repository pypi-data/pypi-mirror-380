"""Libraries"""
import sys
import shutil
from pathlib import Path

import tomli
import typer

from .utils import success_message, error_message
from .dialogs import setup_dialogs, get_description

app = typer.Typer(no_args_is_help=True)

@app.command(name="help")
def help_command():
    """Provides help on usage for pyinp
    """
    sys.argv = [sys.argv[0], "--help"] # Runs help command
    app()

@app.command(name="version")
def version_command():
    """Gets the version of the library
    """
    file = Path(__file__).parent.parent.parent / "pyproject.toml" # pyproject.toml path
    with file.open("rb") as f:
        data = tomli.load(f)

    version = data["project"]["version"] # Library version
    typer.echo(f"pyinp v{version}")

@app.command(name="init")
def init_command():
    """Initializes a new project on the go
    """
    cwd = Path.cwd()

    setup_dialogs("pyproject.toml", cwd, False)
    setup_dialogs("LICENSE", cwd, False)
    setup_dialogs("python-publish.yml", cwd, False)
    setup_dialogs("pylint.yml", cwd, False)
    setup_dialogs(".pylintrc", cwd, False)
    setup_dialogs(".gitignore", cwd, False)
    setup_dialogs("README.md", cwd, False)

@app.command(name="clean")
def clean_command():
    """Cleans useless unwanted files
    """
    cwd = Path.cwd() # Command run location

    cleaned = 0
    failed = 0

    for pattern in ["__pycache__", "*.pyc", "*.pyo", ".pytest_cache", ".mypy_cache", "*.egg-info", "*.log", "*.tmp"]:
        for path in cwd.glob(f"**/{pattern}"):
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
                cleaned += 1
            except Exception as error:
                error_message(error)
                failed += 1

    success_message(f"File(s) Cleaned: {cleaned}\nFile(s) Failed: {failed}") # Shows user how many files have been cleaned

@app.command(name="get-template")
def get_template_command(template: str):
    """Gets a template and adds it to your project

    Args:
        template (str): The template you want to add
    """
    cwd = Path.cwd()
    path = Path(__file__).parent / "templates" # Used for checking if template exists

    for file in path.iterdir(): # Looping through the files
        if file.name == template: # Checking if template exists
            setup_dialogs(file.name, cwd, True)
            return None

    return error_message(f"The template {template} does not exist.")

@app.command(name="templates")
def templates_command():
    """Lists all the available templates
    """
    path = Path(__file__).parent / "templates"
    templates = []

    for i, file in enumerate(path.iterdir()):
        templates.append(f"{i + 1}) {file.name}") # Lists all the available templates

    templates.append("\nAll the templates have been listed!")
    success_message("\n".join(templates))

@app.command(name="template-info")
def template_info_command(template: str):
    """Gets the info on a command

    Args:
        template (str): The template you want to get the info on
    """
    path = Path(__file__).parent / "templates"

    for file in path.iterdir():
        if file.name == template:
            typer.echo(get_description(template)) # Gets the description on templates
            return None

    return error_message(f"The template {template} does not exist.")

if __name__ == "__main__":
    app()
