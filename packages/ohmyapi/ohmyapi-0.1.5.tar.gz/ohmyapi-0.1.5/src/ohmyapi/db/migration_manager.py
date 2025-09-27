import asyncio
from pathlib import Path
from aerich import Command
from ohmyapi.core import runtime


class MigrationManager:
    def __init__(self, project):
        self.project = project
        self._commands = {}
        # Compute tortoise_config grouped by app module
        self._tortoise_config = self._build_tortoise_config()

    def _build_tortoise_config(self) -> dict:
        """
        Build Tortoise config from the flat model_registry,
        grouping models by app module for Aerich compatibility.
        """
        db_url = self.project.settings.DATABASE_URL
        registry = self.project.model_registry  # flat: model_path -> class

        apps_modules = {}
        for model_path, model_cls in registry.items():
            if not isinstance(model_cls, type):
                raise TypeError(f"Registry value must be a class, got {type(model_cls)}: {model_cls}")
            # Extract app module by removing the model class name
            # Example: 'ohmyapi.apps.auth.User' -> 'ohmyapi.apps.auth'
            app_module = ".".join(model_path.split(".")[:-1])
            apps_modules.setdefault(app_module, []).append(model_cls)

        # Build Tortoise config
        apps_config = {}
        for app_module, models in apps_modules.items():
            modules_set = set(m.__module__ for m in models)
            apps_config[app_module] = {
                "models": list(modules_set),
                "default_connection": "default",
            }

        return {
            "connections": {"default": db_url},
            "apps": apps_config,
        }

    def get_apps(self):
        """Return app modules extracted from the registry"""
        return list(self._tortoise_config["apps"].keys())

    def get_migration_location(self, app_module: str) -> str:
        """Return the path to the app's migrations folder"""
        try:
            module = __import__(app_module, fromlist=["migrations"])
            if not hasattr(module, "__file__") or module.__file__ is None:
                raise ValueError(f"Cannot determine filesystem path for app '{app_module}'")
            app_path = Path(module.__file__).parent
            migrations_path = app_path / "migrations"
            migrations_path.mkdir(exist_ok=True)
            return str(migrations_path)
        except ModuleNotFoundError:
            raise ValueError(f"App module '{app_module}' cannot be imported")

    async def init_app_command(self, app_module: str) -> Command:
        """Initialize Aerich command for a specific app module"""
        location = self.get_migration_location(app_module)
        cmd = Command(
            tortoise_config=self._tortoise_config,
            app=app_module,
            location=location,
        )
        await cmd.init()
        self._commands[app_module] = cmd
        return cmd

    async def makemigrations(self, app_module: str):
        """Generate migrations for a specific app"""
        cmd = self._commands.get(app_module) or await self.init_app_command(app_module)
        await cmd.migrate()

    async def migrate(self, app_module: str = None):
        """Apply migrations. If app_module is None, migrate all apps"""
        apps_to_migrate = [app_module] if app_module else self.get_apps()
        for app in apps_to_migrate:
            cmd = self._commands.get(app) or await self.init_app_command(app)
            await cmd.upgrade()

    async def show_migrations(self, app_module: str):
        """List migrations for an app"""
        cmd = self._commands.get(app_module) or await self.init_app_command(app_module)
        await cmd.history()

