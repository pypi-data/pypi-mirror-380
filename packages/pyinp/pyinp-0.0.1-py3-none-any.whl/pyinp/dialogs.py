"""Libraries"""
import shutil
from datetime import datetime
from pathlib import Path

import typer

from .utils import error_message, success_message

descriptions = {
    ".gitignore": "This file tells Git which files and directories to ignore when tracking changes. It keeps your repository clean by preventing temporary files, build artifacts, virtual environments, or personal configuration files from being committed.",
    "LICENSE": "The license file defines the legal terms under which others can use, modify, and distribute your project. It's essential for clarifying permissions, protecting your rights as the author, and encouraging contributions while setting boundaries on usage.",
    ".pylintrc": "This is the configuration file for Pylint, a popular Python code analysis tool. It allows you to customize linting rules, code style checks, and warnings so that they fit your project's standards and maintain code consistency across contributors.",
    "README.md": "The README provides the first impression of your project. It typically includes an overview, installation instructions, usage examples, and any other essential details that help users, collaborators, or contributors understand what your project does and how to work with it.",
    "pyproject.toml": "This file is the central configuration for modern Python projects. It defines metadata (like project name, version, authors), build system requirements, and tool configurations. It serves as a standardized place for Python tooling to understand how to build, install, and manage your project.",
    "pylint.yml": "This file configures Pylint when using it with a CI/CD pipeline or other YAML-based automation. It defines rules, severity levels, and exclusions for code analysis, helping maintain consistent code quality across contributors and automated checks.",
    "python-publish.yml": "This workflow file is typically used in GitHub Actions or similar automation tools to publish a Python package. It defines the steps required to build, test, and release your project, including uploading artifacts to package indexes, making it easier to automate releases and maintain reproducibility."
}

def setup_dialogs(file: str, cwd, msg: bool):
    """Setups the dialog for adding files to the project

    Args:
        file (str): The file to setup
        cwd (_type_): The location cwd
        msg (bool): Whether to have a success message or not
    """
    path = Path(__file__).parent / "templates" / file

    if file not in {"pyproject.toml", "LICENSE", "python-publish.yml", "pylint.yml"}:
        try:
            shutil.copy(path, cwd)
            if msg:
                success_message(f"Successfully added {file} to your project!")
        except Exception as error:
            error_message(error)
    else:
        if file == "pyproject.toml":
            name = typer.prompt("\n\nFirst, let's set the project name. This is the identifier for your project. It's how tools, collaborators, or even automated scripts will refer to it. The name doesn't have to be globally unique, but it should clearly represent your project's purpose. Avoid unnecessary spaces or symbols to keep it compatible across tools.\n\nWhat name would you like to give this project?")
            description = typer.prompt("\n\nNext, we'll write the project description. Think of this as a short summary that explains what your project is about. This can help collaborators, future maintainers, or even your future self quickly understand what the project does without digging through the code.\n\nHow would you describe your project in one or two sentences?")
            author_name = typer.prompt("\n\nNow let's add the author's full name. The author is usually the person or team who originally started the project. This field is mostly informational — it provides context about the origin of the work and gives credit to the initial creator.\n\nWhose name should I list as the author?")
            author_email = typer.prompt("\n\nThanks! Alongside the name, we can include the author's email address. This is optional but useful for contact, attribution, or record-keeping. It could be a personal email, a work email, or even a group inbox if this project belongs to a team.\n\nWhat email should I associate with the author?")
            maintainer_name = typer.prompt("\n\nNow let's set the maintainer name. The maintainer is whoever is currently responsible for keeping the project working — whether that's fixing bugs, updating dependencies, or just ensuring it doesn't break. The maintainer might be the same as the author, or it could be someone else if the project has been handed over.\n\nWho should be listed as the maintainer?")
            maintainer_email = typer.prompt("\n\nAnd finally, let's add the maintainer's email address. This is the primary point of contact for anyone who needs help, has feedback, or wants to coordinate changes. Again, this doesn't have to be personal — it could be an official project email or even a shared team inbox.\n\nWhat email should I assign to the maintainer?")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = f.read()
                    data = data.replace("<PROJECT-NAME>", name)
                    data = data.replace("<PROJECT-DESCRIPTION>", description)
                    data = data.replace("<AUTHOR-NAME>", author_name)
                    data = data.replace("<AUTHOR-EMAIL>", author_email)
                    data = data.replace("<MAINTAINER-NAME>", maintainer_name)
                    data = data.replace("<MAINTAINER-EMAIL>", maintainer_email)

                with open(cwd / file, "w", encoding="utf-8") as f:
                    f.write(data)

                if msg:
                    success_message(f"Successfully added {file} to your project!")
            except Exception as error:
                error_message(error)
        elif file == "LICENSE":
            name = typer.prompt("\n\nLet's add the author name for the license. This name will be used in the license file to indicate who owns the rights to the project. It can be your personal name, your organization, or a team name if the project belongs to a group. Including this helps clarify ownership and makes the license legally meaningful.\n\nWhat name should I put in the license?")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = f.read()
                    data = data.replace("<COPYRIGHT HOLDER>", name)
                    data = data.replace("<YEAR>", str(datetime.now().year))

                with open(cwd / file, "w", encoding="utf-8") as f:
                    f.write(data)

                if msg:
                    success_message(f"Successfully added {file} to your project!")
            except Exception as error:
                error_message(error)
        elif file == "python-publish.yml":
            package_name = typer.prompt("Let's set the package name for your publishing workflow. This is the name of the Python package that will be built and released by the workflow. It should match the project's official name so that automated steps like building, testing, and publishing to package indexes work correctly. Using a clear and consistent name ensures that users and tools can find and install your package without confusion.\n\nWhat should the package name be?")

            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = f.read()
                    data = data.replace("<PACKAGE-NAME>", package_name)

                workflow_path = cwd / ".github" / "workflows" / file
                workflow_path.parent.mkdir(parents=True, exist_ok=True)

                with open(workflow_path, "w", encoding="utf-8") as f:
                    f.write(data)

                if msg:
                    success_message(f"Successfully added {file} to your project!")
            except Exception as error:
                error_message(error)
        elif file == "pylint.yml":
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = f.read()

                workflow_path = cwd / ".github" / "workflows" / file
                workflow_path.parent.mkdir(parents=True, exist_ok=True)

                with open(workflow_path, "w", encoding="utf-8") as f:
                    f.write(data)

                if msg:
                    success_message(f"Successfully added {file} to your project!")
            except Exception as error:
                error_message(error)

def get_description(file: str):
    """Gets description of template

    Args:
        file (str): The template file

    Returns:
        _type_: The description of the template
    """
    for f, description in descriptions.items():
        if f == file:
            return description

    return error_message(f"The description for the template {file}, could not be retrieved.")
