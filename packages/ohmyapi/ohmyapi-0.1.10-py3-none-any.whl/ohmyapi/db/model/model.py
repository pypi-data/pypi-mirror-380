from tortoise import fields as field
from tortoise.models import Model as TortoiseModel
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class ModelMeta(type(TortoiseModel)):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)

        schema_opts = getattr(new_cls, "Schema", None)

        class BoundSchema:
            @property
            def one(self):
                """Return a Pydantic model class for 'one' results."""
                include = getattr(schema_opts, "include", None)
                exclude = getattr(schema_opts, "exclude", None)
                return pydantic_model_creator(
                    new_cls,
                    name=f"{new_cls.__name__}SchemaOne",
                    include=include,
                    exclude=exclude,
                    exclude_readonly=True,
                )

            @property
            def many(self):
                """Return a Pydantic queryset class for 'many' results."""
                include = getattr(schema_opts, "include", None)
                exclude = getattr(schema_opts, "exclude", None)
                return pydantic_queryset_creator(
                    new_cls,
                    name=f"{new_cls.__name__}SchemaMany",
                    include=include,
                    exclude=exclude,
                )

        new_cls.Schema = BoundSchema()
        return new_cls


class Model(TortoiseModel, metaclass=ModelMeta):
    class Schema:
        include = None
        exclude = None

