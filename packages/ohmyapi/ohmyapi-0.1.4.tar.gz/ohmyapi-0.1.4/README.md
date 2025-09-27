# OhMyAPI

> OhMyAPI == Application scaffolding for FastAPI+TortoiseORM.

OhMyAPI is a Django-flavored web-application scaffolding framework.
Built around FastAPI and TortoiseORM, it 100% async.
It is blazingly fast and has batteries included.

Features:

- Django-like project-layout and -structure
- Django-like settings.py
- Django-like models via TortoiseORM
- Django-like model.Meta class for model configuration
- Django-like advanced permissions system
- Django-like migrations (makemigrations & migrate) via Aerich
- Django-like CLI for interfacing with your projects (startproject, startapp, shell, serve, etc)
- various optional builtin apps
- highly configurable and customizable
- 100% async

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
ohmyapi startapp myapp
```

This will lead to the following directory structure:

```
myproject/
  - myapp/
    - __init__.py
    - models.py
    - routes.py
  - pyproject.toml
  - settings.py
```

Add 'myapp' to your `INSTALLED_APPS` in `settings.py`.

Write your first model in `myapp/models.py`:

```python
from ohmyapi.db import Model, field


class Person(Model):
    id: int = field.IntField(min=1, pk=True)
    name: str = field.CharField(min_length=1, max_length=255)
    username: str = field.CharField(min_length=1, max_length=255, unique=True)
    age: int = field.IntField(min=0)
```

Next, create your endpoints in `myapp/routes.py`:

```python
from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from .models import Person

router = APIRouter(prefix="/myapp")


@router.get("/")
async def list():
    return await Person.Schema.many.from_queryset(Person.all())


@router.get("/:id")
async def get(id: int):
    try:
        return await Person.Schema.one(Person.get(pk=id))
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
  - myapp/
    - __init__.py
    - models.py
    - routes.py
  - migrations/
    - myapp/
  - pyproject.toml
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
Remember to `makemigrations` and `migrate` for the auth tables to be created in the database.

`settings.py`:

```
INSTALLED_APPS = [
    'ohmyapi_auth',
    ...
]

JWT_SECRET = "t0ps3cr3t"
```

Create a super-user:

```
ohmyapi createsuperuser
```

