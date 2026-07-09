from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


def utcnow():
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(
        DateTime,
        default=utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=utcnow,
        onupdate=utcnow,
        nullable=False
    )


class Employee(BaseModel):
    __tablename__ = 'employees'

    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
