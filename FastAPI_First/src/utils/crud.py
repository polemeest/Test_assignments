"""
CRUD
"""

from sqlalchemy.orm import Session
from apps.lovers import models, schemas


def get_lover(db: Session, lover_id: int):
    return db.query(models.Lover).filter(models.Lover.id == lover_id).first()


def get_lovers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lover).offset(skip).limit(limit).all()


def get_lover_by_email(db: Session, email: str):
    return db.query(models.Lover).filter(models.Lover.email == email).first()


def create_lover(db: Session, lover: schemas.LoverCreate):
    hashing = hash(lover.hashed_password)
    db_lover = models.Lover(email=lover.email, hashed_password=hashing)
    db.add(db_lover)
    db.commit()
    db.refresh(db_lover)
    return db_lover


def get_actions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Action).offset(skip).limit(limit).all()


def create_action(db: Session, action: schemas.ActionCreate, lover_id: int):
    db_action = models.Action(action.model_dump, lover_id=lover_id)
    db.add(db_action)
    db.commit()
    db.refresh()
    return db_action