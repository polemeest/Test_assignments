from pydantic import BaseModel


class ActionBase(BaseModel):
    title: str
    description: str


class ActionCreate(ActionBase):
    pass


class Action(ActionBase):
    id: int
    lover_id: int | None = None

    class Config:
        orm_mode = True



class LoverBase(BaseModel):
    email: str


class LoverCreate(LoverBase):
    hashed_password: str


class Lover(LoverBase):
    id: int
    is_active: bool
    actions: list[Action] = []

    class Config:
        orm_mode = True