import asyncio
import atexit
import importlib
import sys
from getpass import getpass
from pathlib import Path

import typer
import uvicorn

from ohmyapi.core import runtime, scaffolding

app = typer.Typer(
    help="OhMyAPI — Django-flavored FastAPI scaffolding with tightly integrated TortoiseORM."
)


@app.command()
def startproject(name: str):
    """Create a new OhMyAPI project in the given directory."""
    scaffolding.startproject(name)


@app.command()
def startapp(app_name: str, root: str = "."):
    """Create a new app with the given name in your OhMyAPI project."""
    scaffolding.startapp(app_name, root)


@app.command()
def serve(root: str = ".", host="127.0.0.1", port=8000):
    """
    Run this project in via uvicorn.
    """
    project_path = Path(root)
    project = runtime.Project(project_path)
    app_instance = project.app()
    uvicorn.run(app_instance, host=host, port=int(port), reload=False)


@app.command()
def shell(root: str = "."):
    project_path = Path(root).resolve()
    project = runtime.Project(project_path)

    banner = f"""
    OhMyAPI Project Shell: {getattr(project.settings, 'PROJECT_NAME', 'MyProject')}
    Find your loaded project singleton via identifier: `p`; i.e.: `p.apps`
    """

    async def init_and_cleanup():
        try:
            await project.init_orm()
            return True
        except Exception as e:
            print(f"Failed to initialize ORM: {e}")
            return False

    async def cleanup():
        try:
            await project.close_orm()
            print("Tortoise ORM closed successfully.")
        except Exception as e:
            print(f"Error closing ORM: {e}")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(init_and_cleanup())

    # Prepare shell vars that are to be directly available
    shell_vars = {"p": project}

    try:
        from IPython import start_ipython
        from traitlets.config.loader import Config

        c = Config()
        c.TerminalIPythonApp.display_banner = True
        c.TerminalInteractiveShell.banner2 = banner

        start_ipython(argv=[], user_ns=shell_vars, config=c)
    except ImportError:
        import code

        code.interact(local=shell_vars, banner=banner)
    finally:
        loop.run_until_complete(cleanup())


@app.command()
def makemigrations(app: str = "*", name: str = "auto", root: str = "."):
    """
    Create a DB migration based on your models.
    """
    project_path = Path(root).resolve()
    project = runtime.Project(project_path)
    if app == "*":
        for app in project.apps.keys():
            asyncio.run(project.makemigrations(app_label=app, name=name))
    else:
        asyncio.run(project.makemigrations(app_label=app, name=name))


@app.command()
def migrate(app: str = "*", root: str = "."):
    """
    Run all DB migrations.
    """
    project_path = Path(root).resolve()
    project = runtime.Project(project_path)
    if app == "*":
        for app in project.apps.keys():
            asyncio.run(project.migrate(app))
    else:
        asyncio.run(project.migrate(app))


@app.command()
def createsuperuser(root: str = "."):
    """Create a superuser in the DB.

    This requires the presence of `ohmyapi_auth` in your INSTALLED_APPS to work.
    """
    project_path = Path(root).resolve()
    project = runtime.Project(project_path)
    if not project.is_app_installed("ohmyapi_auth"):
        print(
            "Auth app not installed! Please add 'ohmyapi_auth' to your INSTALLED_APPS."
        )
        return

    import asyncio

    import ohmyapi_auth

    email = input("E-Mail: ")
    username = input("Username: ")
    password1, password2 = "foo", "bar"
    while password1 != password2:
        password1 = getpass("Password: ")
        password2 = getpass("Repeat Password: ")
        if password1 != password2:
            print("Passwords didn't match!")
    user = ohmyapi_auth.models.User(
        email=email, username=username, is_staff=True, is_admin=True
    )
    user.set_password(password1)
    asyncio.run(project.init_orm())
    asyncio.run(user.save())
    asyncio.run(project.close_orm())
