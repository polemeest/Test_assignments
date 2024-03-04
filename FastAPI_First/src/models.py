from pydantic import BaseModel

class Lovers(BaseModel):
    name: str
    action: str | None