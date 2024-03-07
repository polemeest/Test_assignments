from fastapi import APIRouter
from pathlib import Path
from datetime import datetime

from utils.enums import Names


if not __name__ == '__main__': Path(__file__).resolve()
router = APIRouter(
    prefix="",
    tags=["singletons"],
    responses={404: {"description": "Not found"}},
)

@router.get("/today")
async def show_current_date() -> str:
    return datetime.strftime(datetime.now(), "%d/%m/%Y, %H:%M:%S")


@router.get("/multiply/{number}")
async def multiply(number: int) -> dict[str, int]:
    return {"number": number,
            "powered": number ** 2}


@router.get("/names/{name}")
async def enums(name: Names) -> str:
    return f"Greetings, {name}! Love you!"


@router.get("/path/{urlpath:path}")
async def path_resolve(urlpath: str) -> dict[str, str]:
    return {"your path is": urlpath}


@router.get("/query/{some}")
async def queries(some: str,
                  query: int = 10,
                  query2: str | None = None,
                  query3: bool = False) -> str:
    return f"{some}, {query}, {query2}, {query3}"