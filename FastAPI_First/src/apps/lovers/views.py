from fastapi import APIRouter
from pathlib import Path
from typing import Any

from .serializers import Lovers


if not __name__ == '__main__': Path(__file__).resolve()
router = APIRouter(
    prefix="/lovers",
    tags=["lovers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_lovers(
    lover: Lovers | None = Lovers(name="Denis", action="kisses_Eva"), 
    another: Lovers | None = Lovers(name="Eva", action="kisses Denis")) -> str:    
    return f"{lover}, {another}"


@router.post("/")
async def post_lovers(lover: Lovers) -> str | Lovers | None:
    return lover


@router.put("/{lover_id}")
async def get_lovers_id(lover_id: int, lover: Lovers) -> dict[str, Any]:
    return {"id": lover_id, "lover": lover.model_dump()}