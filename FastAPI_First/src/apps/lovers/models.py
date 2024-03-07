from sqlalchemy import Boolean, Column, ForeignKey, String, SmallInteger, Text
from sqlalchemy.orm import relationship

from utils.database import Base


class Lover(Base):
    __tablename__ = "lovers"

    id = Column(SmallInteger, primary_key=True)
    email = Column(String, default='', index=True)
    hashed_password = Column(String, unique=True)
    is_active = Column(Boolean, default=False)

    actions = relationship("Action", back_populates="lover")


class Action(Base):
    __tablename__ = "actions"

    id = Column(SmallInteger, primary_key=True)
    title = Column(String, index=True)
    description = Column(Text, index=True)
    lover_id = Column(SmallInteger, ForeignKey("lovers.id"))

    lover = relationship("Lover", back_populates="action")

