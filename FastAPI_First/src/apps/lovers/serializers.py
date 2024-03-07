from pydantic import BaseModel
from pathlib import Path


print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())


class Lovers(BaseModel):
    name: str
    action: str | None