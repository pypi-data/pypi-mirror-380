import asyncio
import atexit
import importlib
import sys
import typer
import uvicorn

from getpass import getpass
from ohmyapi.core import scaffolding, runtime
from pathlib import Path

app = typer.Typer(help="OhMyAPI — Django-flavored FastAPI scaffolding with tightly integrated TortoiseORM.")
banner = """OhMyAPI Shell | Project: {project_name}
Find your loaded project singleton via identifier: `p`
"""


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
    """
    Launch an interactive IPython shell with the project and apps loaded.
    """
    project_path = Path(root).resolve()
    project = runtime.Project(project_path)

    # Ensure the ORM is shutdown
    async def close_project():
        try:
            await project.close_orm()
            print("Tortoise ORM closed successfully.")
        except Exception as e:
            print(f"Error closing ORM: {e}")

    def cleanup():
        loop = None
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            pass
        if loop and loop.is_running():
            asyncio.create_task(close_project())
        else:
            asyncio.run(close_project())

    # Ensure the ORM is initialized
    asyncio.run(project.init_orm())

    try:
        from IPython import start_ipython
        shell_vars = {
            "p": project,
        }
        from traitlets.config.loader import Config
        c = Config()
        c.TerminalIPythonApp.display_banner = True
        c.TerminalInteractiveShell.banner2 = banner.format(**{
            "project_name": f"{f'{project.settings.PROJECT_NAME} ' if getattr(project.settings, 'PROJECT_NAME', '') else ''}[{Path(project_path).resolve()}]",
        })
        atexit.register(cleanup)
        start_ipython(argv=[], user_ns=shell_vars, config=c)
    except ImportError:
        typer.echo("IPython is not installed. Falling back to built-in Python shell.")
        import code
        atexit.register(cleanup)
        code.interact(local={"p": project})


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
        print("Auth app not installed! Please add 'ohmyapi_auth' to your INSTALLED_APPS.")
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
    user = ohmyapi_auth.models.User(email=email, username=username, is_staff=True, is_admin=True)
    user.set_password(password1)
    asyncio.run(project.init_orm())
    asyncio.run(user.save())
    asyncio.run(project.close_orm())

