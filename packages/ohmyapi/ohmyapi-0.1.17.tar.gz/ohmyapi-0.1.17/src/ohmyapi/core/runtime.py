# ohmyapi/core/runtime.py
import copy
import importlib
import importlib.util
import pkgutil
import sys
from pathlib import Path
from typing import Dict, List, Optional

import click
from aerich import Command as AerichCommand
from aerich.exceptions import NotInitedError
from tortoise import Tortoise
from fastapi import FastAPI, APIRouter
from ohmyapi.db.model import Model


class Project:
    """
    Project runtime loader + Tortoise/Aerich integration.

    - injects builtin apps as ohmyapi_<name>
    - builds unified tortoise config for runtime
    - provides makemigrations/migrate methods using Aerich Command API
    """

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self._apps: Dict[str, App] = {}
        self.migrations_dir = self.project_path / "migrations"

        if str(self.project_path) not in sys.path:
            sys.path.insert(0, str(self.project_path))

        # Pre-register builtin apps as ohmyapi_<name>.
        # This makes all builtin apps easily loadable via f"ohmyapi_{app_name}".
        spec = importlib.util.find_spec("ohmyapi.builtin")
        if spec and spec.submodule_search_locations:
            for _, modname, _ in pkgutil.iter_modules(spec.submodule_search_locations):
                full = f"ohmyapi.builtin.{modname}"
                alias = f"ohmyapi_{modname}"
                if alias not in sys.modules:
                    orig = importlib.import_module(full)
                    sys.modules[alias] = orig
                    try:
                        sys.modules[f"{alias}.models"] = importlib.import_module(f"{full}.models")
                    except ModuleNotFoundError:
                        pass

        # Load settings.py
        try:
            self.settings = importlib.import_module("settings")
        except Exception as e:
            raise RuntimeError(f"Failed to import project settings from {self.project_path}") from e

        # Load installed apps
        for app_name in getattr(self.settings, "INSTALLED_APPS", []):
            self._apps[app_name] = App(self, name=app_name)

    @property
    def apps(self):
        return self._apps

    def is_app_installed(self, name: str) -> bool:
        return name in getattr(self.settings, "INSTALLED_APPS", [])

    def app(self, generate_schemas: bool = False) -> FastAPI:
        """
        Create a FastAPI app, attach all APIRouters from registered apps,
        and register ORM lifecycle event handlers.
        """
        app = FastAPI(title=getattr(self.settings, "PROJECT_NAME", "OhMyAPI Project"))

        # Attach routers from apps
        for app_name, app_def in self._apps.items():
            if app_def.router:
                app.include_router(app_def.router)

        # Startup / shutdown events
        @app.on_event("startup")
        async def _startup():
            await self.init_orm(generate_schemas=generate_schemas)

        @app.on_event("shutdown")
        async def _shutdown():
            await self.close_orm()

        return app

    # --- Config builders ---
    def build_tortoise_config(self, db_url: Optional[str] = None) -> dict:
        """
        Build unified Tortoise config for all registered apps.
        """
        db = db_url or getattr(self.settings, "DATABASE_URL", "sqlite://db.sqlite3")
        config = {
            "connections": {"default": db},
            "apps": {},
            "tortoise": "Tortoise",
            "migrations_dir": str(self.migrations_dir),
        }

        for app_name, app in self._apps.items():
            modules = list(dict.fromkeys(app.model_modules))
            if modules:
                config["apps"][app_name] = {"models": modules, "default_connection": "default"}

        return config

    def build_aerich_command(self, app_label: str, db_url: Optional[str] = None) -> AerichCommand:
        # Resolve label to flat_label
        if app_label in self._apps:
            flat_label = app_label
        else:
            candidate = app_label.replace(".", "_")
            if candidate in self._apps:
                flat_label = candidate
            else:
                raise RuntimeError(f"App '{app_label}' is not registered")

        # Get a fresh copy of the config (without aerich.models anywhere)
        tortoise_cfg = copy.deepcopy(self.build_tortoise_config(db_url=db_url))

        # Append aerich.models to the models list of the target app only
        if flat_label in tortoise_cfg["apps"]:
            tortoise_cfg["apps"][flat_label]["models"].append("aerich.models")

        return AerichCommand(
            tortoise_config=tortoise_cfg,
            app=flat_label,
            location=str(self.migrations_dir)
        )

    # --- ORM lifecycle ---
    async def init_orm(self, generate_schemas: bool = False) -> None:
        if not Tortoise.apps:
            cfg = self.build_tortoise_config()
            await Tortoise.init(config=cfg)
            if generate_schemas:
                await Tortoise.generate_schemas(safe=True)

    async def close_orm(self) -> None:
        await Tortoise.close_connections()

    # --- Migration helpers ---
    async def makemigrations(self, app_label: str, name: str = "auto", db_url: Optional[str] = None) -> None:
        cmd = self.build_aerich_command(app_label, db_url=db_url)
        async with cmd as c:
            await c.init()
            try:
                await c.init_db(safe=True)
            except FileExistsError:
                pass
            try:
                await c.migrate(name=name)
            except (NotInitedError, click.UsageError):
                await c.init_db(safe=True)
                await c.migrate(name=name)

    async def migrate(self, app_label: Optional[str] = None, db_url: Optional[str] = None) -> None:
        labels: List[str]
        if app_label:
            if app_label in self._apps:
                labels = [app_label]
            else:
                raise RuntimeError(f"Unknown app '{app_label}'")
        else:
            labels = list(self._apps.keys())

        for lbl in labels:
            cmd = self.build_aerich_command(lbl, db_url=db_url)
            async with cmd as c:
                await c.init()
                try:
                    await c.init_db(safe=True)
                except FileExistsError:
                    pass

                try:
                    # Try to apply migrations
                    await c.upgrade()
                except (NotInitedError, click.UsageError):
                    # No migrations yet, initialize then retry upgrade
                    await c.init_db(safe=True)
                    await c.upgrade()


class App:
    """App container holding runtime data like detected models and routes."""

    def __init__(self, project: Project, name: str):
        self.project = project
        self.name = name

        # The list of module paths (e.g. "ohmyapi_auth.models") for Tortoise and Aerich
        self.model_modules: List[str] = []

        # The APIRouter
        self.router: Optional[APIRouter] = None

        # Import the app, so its __init__.py runs.
        importlib.import_module(self.name)

        # Load the models
        try:
            models_mod = importlib.import_module(f"{self.name}.models")
            self.model_modules.append(f"{self.name}.models")
        except ModuleNotFoundError:
            pass

        # Locate the APIRouter
        try:
            routes_mod = importlib.import_module(f"{self.name}.routes")
            router = getattr(routes_mod, "router", None)
            if isinstance(router, APIRouter):
                self.router = router
        except ModuleNotFoundError:
            pass

    def __repr__(self):
        out = ""
        out += f"App: {self.name}\n"
        out += f"Models:\n"
        for model in self.models:
            out += f" - {model.__name__}\n"
        out += "Routes:\n"
        for route in (self.routes or []):
            out += f" - {route}\n"
        return out

    def __str__(self):
        return self.__repr__()

    @property
    def models(self) -> List[Model]:
        models: List[Model] = []
        for mod in self.model_modules:
            models_mod = importlib.import_module(mod)
            for obj in models_mod.__dict__.values():
                if isinstance(obj, type) and getattr(obj, "_meta", None) is not None and obj.__name__ != 'Model':
                    models.append(obj)
        return models

    @property
    def routes(self):
        return self.router.routes

