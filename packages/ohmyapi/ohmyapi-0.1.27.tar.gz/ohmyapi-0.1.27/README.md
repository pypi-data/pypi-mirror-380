# OhMyAPI

> Think: Django RestFramework, but less clunky and 100% async.

OhMyAPI is a Django-flavored web-application scaffolding framework and management layer,
built around FastAPI and TortoiseORM and is thus 100% async.

It is ***blazingly fast***, extremely ***fun to use*** and comes with ***batteries included***!

**Features**

- Django-like project structure and application directories
- Django-like per-app migrations (`makemigrations` & `migrate`) via Aerich
- Django-like CLI tooling (`startproject`, `startapp`, `shell`, `serve`, etc)
- Customizable pydantic model serializer built-in 
- Various optional built-in apps you can hook into your project
- Highly configurable and customizable
- 100% async

**Goals**

- combine `FastAPI`, `TortoiseORM`, `Aerich` migrations and `Pydantic` into a high-productivity web-application framework
- tie everything neatly together into a concise and straight-forward API
- ***AVOID*** adding any abstractions on top, unless they make things extremely convenient

---

## Getting started

**Creating a Project**

```
pipx install ohmyapi
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

from datetime import datetime
from decimal import Decimal
from uuid import UUID


class Tournament(Model):
    id: UUID = field.data.UUIDField(primary_key=True)
    name: str = field.TextField()
    created: datetime = field.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(Model):
    id: UUID = field.data.UUIDField(primary_key=True)
    name: str = field.TextField()
    tournament: UUID = field.ForeignKeyField('tournament.Tournament', related_name='events')
    participants: field.ManyToManyRelation[Team] = field.ManyToManyField('tournament.Team', related_name='events', through='event_team')
    modified: datetime = field.DatetimeField(auto_now=True)
    prize: Decimal = field.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Team(Model):
    id: UUID = field.data.UUIDField(primary_key=True)
    name: str = field.TextField()

    def __str__(self):
        return self.name
```

### API Routes

Next, create your endpoints in `tournament/routes.py`:

```python
from ohmyapi.router import APIRouter, HTTPException, HTTPStatus
from ohmyapi.db.exceptions import DoesNotExist

from typing import List

from .models import Tournament

# OhMyAPI will automatically pick up all instances of `fastapi.APIRouter` and
# add their routes to the main project router.
#
# Note:
# Use prefixes wisely to avoid cross-app namespace-collisions!
# Tags improve the UX of the OpenAPI docs at /docs.
#
tournament_router = APIRouter(prefix="/tournament", tags=['Tournament'])


@tournament_router.get("/", response_model=List[Tournament.Schema()])
async def list():
    queryset = Tournament.all()
    return await Tournament.Schema.model.from_queryset(queryset)


@tournament_router.post("/", status_code=HTTPStatus.CREATED)
async def post(tournament: Tournament.Schema(readonly=True)):
    queryset = Tournament.create(**payload.model_dump())
    return await Tournament.Schema().from_queryset(queryset)


@tournament_router.get("/:id", response_model=Tournament.Schema())
async def get(id: str):
    try:
        queryset = Tournament.get(id=id)
        return await Tournament.Schema().from_queryset_single(tournament)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="not found")


@tournament_router.delete("/:id")
async def delete(id: str):
    try:
        tournament = await Tournament.get(id=id)
        return await Tournament.Schema.model.from_queryset(tournament.delete())
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="not found")


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
from ohmyapi.db import Model, field
from ohmyapi_auth.models import User


class Team(Model):
    [...]
    members: field.ManyToManyRelation[User] = field.ManyToManyField('ohmyapi_auth.User', related_name='tournament_teams', through='tournament_teams')
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
from ohmyapi_auth import (
    models as auth,
    permissions,
)

from .models import Tournament

router = APIRouter(prefix="/tournament", tags=["Tournament"])


@router.get("/")
async def list(user: auth.User = Depends(permissions.require_authenticated)):
    queryset = Tournament.all()
    return await Tournament.Schema().from_queryset(queryset)


...
```

### Model-Level Permissions

Use Tortoise's `Manager` to implement model-level permissions.

```python
from ohmyapi.db import Manager
from ohmyapi_auth.models import User


class TeamManager(Manager):
    async def for_user(self, user: User):
        return await self.filter(members=user).all()


class Team(Model):
    [...]

    class Meta:
        manager = TeamManager()
```

Use the custom manager in your FastAPI route handler:

```python
from ohmyapi.router import APIRouter
from ohmyapi_auth import (
    models as auth,
    permissions,
)

router = APIRouter(prefix="/tournament", tags=["Tournament"])


@router.get("/teams")
async def teams(user: auth.User = Depends(permissions.require_authenticated)):
    queryset = Team.for_user(user)
    return await Tournament.Schema().from_queryset(queryset)
```

## Shell

Similar to Django, you can attach to an interactive shell with your project already loaded inside.

```
ohmyapi shell

Python 3.13.7 (main, Aug 15 2025, 12:34:02) [GCC 15.2.1 20250813]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.5.0 -- An enhanced Interactive Python. Type '?' for help.

OhMyAPI Shell | Project: {{ project_name }} [{{ project_path }}]
Find your loaded project singleton via identifier: `p`
```

```python
In [1]: p
Out[1]: <ohmyapi.core.runtime.Project at 0x7f00c43dbcb0>

In [2]: p.apps
Out[2]:
{'ohmyapi_auth': {
   "models": [
     "Group",
     "User"
   ],
   "routes": [
     {
       "path": "/auth/login",
       "name": "login",
       "methods": [
         "POST"
       ],
       "endpoint": "login",
       "response_model": null,
       "tags": [
         "auth"
       ]
     },
     {
       "path": "/auth/refresh",
       "name": "refresh_token",
       "methods": [
         "POST"
       ],
       "endpoint": "refresh_token",
       "response_model": null,
       "tags": [
         "auth"
       ]
     },
     {
       "path": "/auth/introspect",
       "name": "introspect",
       "methods": [
         "GET"
       ],
       "endpoint": "introspect",
       "response_model": null,
       "tags": [
         "auth"
       ]
     },
     {
       "path": "/auth/me",
       "name": "me",
       "methods": [
         "GET"
       ],
       "endpoint": "me",
       "response_model": null,
       "tags": [
         "auth"
       ]
     }
   ]
 }}
```

