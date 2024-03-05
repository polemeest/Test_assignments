from fastapi import FastAPI
from datetime import datetime
from enum import StrEnum
from typing import Any

from models.pydantic import Lovers



app = FastAPI()

class Names(StrEnum):
    denis = "Denis"
    eva = "Evka"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/today")
async def show_current_date() -> str:
    return datetime.strftime(datetime.now(), "%d/%m/%Y, %H:%M:%S")


@app.get("/lovers")
async def get_lovers(
    lover: Lovers | None = Lovers(name="Denis", action="kisses_Eva"), 
    another: Lovers | None = Lovers(name="Eva", action="kisses Denis")) -> str:    
    return f"{lover}, {another}"


@app.post("/lovers")
async def post_lovers(lover: Lovers) -> str | Lovers | None:
    return lover


@app.put("/lovers/{lover_id}")
async def get_lovers_id(lover_id: int, lover: Lovers) -> dict[str, Any]:
    return {"id": lover_id, "lover": lover.model_dump()}


@app.get("/{number}")
async def multiply(number: int) -> dict[str, int]:
    return {"number": number,
            "powered": number ** 2}


@app.get("/names/{name}")
async def enums(name: Names) -> str:
    return f"Greetings, {name}! Love you!"


@app.get("/path/{urlpath:path}")
async def path_resolve(urlpath: str) -> dict[str, str]:
    return {"your path is": urlpath}


@app.get("/query/{some}")
async def queries(some: str,
                  query: int = 10,
                  query2: str | None = None,
                  query3: bool = False) -> str:
    return f"{some}, {query}, {query2}, {query3}"


