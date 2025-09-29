from ohmyapi.router import APIRouter, HTTPException, HTTPStatus
from ohmyapi.db.exceptions import DoesNotExist

from . import models

from typing import List

# Expose your app's routes via `router = fastapi.APIRouter`.
# Use prefixes wisely to avoid cross-app namespace-collisions.
# Tags improve the UX of the OpenAPI docs at /docs.
router = APIRouter(prefix="/tournemant")


@router.get("/",
            tags=["tournament"],
            response_model=List[models.Tournament.Schema.model])
async def list():
    """List all tournaments."""
    return await models.Tournament.Schema.model.from_queryset(Tournament.all())


@router.post("/",
             tags=["tournament"],
             status_code=HTTPStatus.CREATED)
async def post(tournament: models.Tournament.Schema.readonly):
    """Create tournament."""
    return await models.Tournament.Schema.model.from_queryset(models.Tournament.create(**tournament.model_dump()))


@router.get("/{id}",
            tags=["tournament"],
            response_model=models.Tournament.Schema.model)
async def get(id: str):
    """Get tournament by id."""
    return await models.Tournament.Schema.model.from_queryset(models.Tournament.get(id=id))


@router.put("/{id}",
            tags=["tournament"],
            response_model=models.Tournament.Schema.model,
            status_code=HTTPStatus.ACCEPTED)
async def put(tournament: models.Tournament.Schema.model):
    """Update tournament."""
    return await models.Tournament.Schema.model.from_queryset(models.Tournament.update(**tournament.model_dump()))


@router.delete("/{id}", tags=["tournament"])
async def delete(id: str):
    try:
        tournament = await models.Tournament.get(id=id)
        return await tournament.delete()
    except DoesNotExist:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="not found")

