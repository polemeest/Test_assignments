from fastapi import APIRouter, Depends, HTTPException
from pathlib import Path
from sqlalchemy.orm import Session

from utils.database import get_db
from utils.crud import get_lover, get_lovers, get_lover_by_email, create_lover
from .schemas import Lover, LoverCreate


if not __name__ == '__main__': Path(__file__).resolve()


router = APIRouter(
    prefix="/lovers",
    tags=["lovers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Lover])
async def read_lovers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lovers = get_lovers(db=db, skip=skip, limit=limit)
    return lovers


@router.post("/", response_model=Lover)
async def create_lover_path(lover: LoverCreate, db: Session = Depends(get_db)):
    lover = get_lover_by_email(db=db, email=lover.email)
    print(lover)
    if lover: 
        raise HTTPException(status_code=400, detail="Lover is already registered")
    try:
        return create_lover(db, lover)
    except Exception:
        print("FUCK")


@router.get("/{lover_id}", response_model=Lover)
async def get_lovers_id(lover_id: int, db: Session = Depends(get_db)):
    lover = get_lover(db, lover_id)
    if lover is None:
        raise HTTPException(404, "Lover is not present")
    return lover