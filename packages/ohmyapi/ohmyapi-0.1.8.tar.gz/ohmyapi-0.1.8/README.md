# OhMyAPI

> Think: Django RestFramework, but less clunky and 100% async.

OhMyAPI is a Django-flavored web-application scaffolding framework and management layer.
Built around FastAPI and TortoiseORM, it is 100% async.

It is ***blazingly fast***, ***fun to use*** and comes with ***batteries included***!

**Features**

- Django-like project-layout and -structure
- Django-like project-level settings.py
- Django-like models via TortoiseORM
- Django-like `Model.Meta` class for model configuration
- Easily convert your query results to `pydantic` models via `Model.Schema`
- Django-like migrations (`makemigrations` & `migrate`) via Aerich
- Django-like CLI tooling (`startproject`, `startapp`, `shell`, `serve`, etc)
- Various optional builtin apps you can hook into your project
- Highly configurable and customizable
- 100% async

OhMyAPI aims to:

- combine FastAPI, TortoiseORM and Aerich migrations into a high-productivity web-application framework
- tying everything neatly together into a project structure consisting of apps with models and a router
- while ***AVOIDING*** to introduce any additional abstractions ontop of Tortoise's model-system or FastAPI's routing

---

## Getting started

**Creating a Project**

```
pip install ohmyapi
ohmyapi startproject myproject
cd myproject
```

This will create the following directory structure:

```
myproject/
  - pyproject.toml
  - README.md
  - settings.py
```

Run your project with:

```
ohmyapi serve
```

In your browser go to:
- http://localhost:8000/docs

**Creating an App**

Create a new app by:

```
ohmyapi startapp tournament
```

This will create the following directory structure:

```
myproject/
  - tournament/
    - __init__.py
    - models.py
    - routes.py
  - pyproject.toml
  - README.md
  - settings.py
```

Add 'tournament' to your `INSTALLED_APPS` in `settings.py`.

### Models

Write your first model in `turnament/models.py`:

```python
from ohmyapi.db import Model, field


class Tournament(Model):
    id = field.data.UUIDField(primary_key=True)
    name = field.TextField()
    created = field.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(Model):
    id = field.data.UUIDField(primary_key=True)
    name = field.TextField()
    tournament = field.ForeignKeyField('tournament.Tournament', related_name='events')
    participants = field.ManyToManyField('torunament.Team', related_name='events', through='event_team')
    modified = field.DatetimeField(auto_now=True)
    prize = field.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Team(Model):
    id = field.data.UUIDField(primary_key=True)
    name = field.TextField()

    def __str__(self):
        return self.name
```

### API Routes

Next, create your endpoints in `tournament/routes.py`:

```python
from ohmyapi.router import APIRouter, HTTPException
from ohmyapi.db.exceptions import DoesNotExist

from .models import Tournament

router = APIRouter(prefix="/tournament")


@router.get("/")
async def list():
    queryset = Tournament.all()
    return await Tournament.Schema.many.from_queryset(queryset)


@router.get("/:id")
async def get(id: str):
    try:
        queryset = Tournament.get(pk=id)
        return await Tournament.Schema.one(queryset)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="item not found")

...
```

## Migrations

Before we can run the app, we need to create and initialize the database.

Similar to Django, first run:

```
ohmyapi makemigrations [ <app> ]  # no app means all INSTALLED_APPS
```

This will create a `migrations/` folder in you project root.

```
myproject/
  - tournament/
    - __init__.py
    - models.py
    - routes.py
  - migrations/
    - tournament/
  - pyproject.toml
  - README.md
  - settings.py
```

Apply your migrations via:

```
ohmyapi migrate [ <app> ]  # no app means all INSTALLED_APPS
```

Run your project:

```
ohmyapi serve
```

## Shell

Similar to Django, you can attach to an interactive shell with your project already loaded inside.

```
ohmyapi shell
```

## Authentication

A builtin auth app is available.

Simply add `ohmyapi_auth` to your INSTALLED_APPS and define a JWT_SECRET in your `settings.py`.
Remember to `makemigrations` and `migrate` for the necessary tables to be created in the database.

`settings.py`:

```
INSTALLED_APPS = [
    'ohmyapi_auth',
    ...
]

JWT_SECRET = "t0ps3cr3t"
```

After restarting your project you will have access to the `ohmyapi_auth` app.
It comes with a `User` and `Group` model, as well as endpoints for JWT auth.

You can use the models as `ForeignKeyField` in your application models:

```python
class Team(Model):
    [...]
    members = field.ManyToManyField('ohmyapi_auth.User', related_name='tournament_teams', through='tournament_teams')
    [...]
```

Remember to run `makemigrations` and `migrate` in order for your model changes to take effect in the database.

Create a super-user:

```
ohmyapi createsuperuser
```

## Permissions

### API-Level Permissions

Use FastAPI's `Depends` pattern to implement API-level access-control.


In your `routes.py`:

```python
from ohmyapi.router import APIRouter, Depends

from ohmyapi_auth.models import User
from ohmyapi_auth import (
    models as auth,
    permissions,
)

from .models import Tournament

router = APIRouter(prefix="/tournament")


@router.get("/")
async def list(user: auth.User = Depends(permissions.require_authenticated)):
    queryset = Tournament.all()
    return await Tournament.Schema.many.from_queryset(queryset)


...
```

### Model-Level Permissions

Use Tortoise's `Manager` to implement model-level permissions.

```python
from ohmyapi.db import Manager
from typing import Callable


class TeamManager(Manager):
    async def for_user(self, user: ohmyapi_auth.models.User):
        return await self.filter(members=user).all()


class Team(Model):
    [...]

    class Meta:
        manager = TeamManager()
```
