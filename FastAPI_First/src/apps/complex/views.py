from fastapi import APIRouter, Query
from pathlib import Path
from typing import Annotated


if not __name__ == '__main__': Path(__file__).resolve()
router = APIRouter(
    prefix="/complex",
    tags=["complex"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def annotated(r: Annotated[str | None, Query(min_length=3)],
                    q: Annotated[str | None, 
                        Query(max_length=50)] = None):
    return f"{q}, {r}"



@router.get("/list")
async def query_list(r: Annotated[str | None, Query(min_length=3)],
                q: Annotated[list[str], Query(max_length=5)] = None):
    return {"q": q, "r": r}


@router.get("/desc")
async def description(q: Annotated[list[str], 
                        Query(max_length=5,
                              title="Worth of the cake",
                              description="No one knows if the cake\
                                is worth buying")] = None):
    return {"q": q}


@router.get("/depr")
async def deprecated(q: Annotated[list[str], 
                        Query(max_length=5,
                              deprecated=True)]):
    return {"q": q}
