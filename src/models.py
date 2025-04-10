from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):
    @declared_attr
    def id(cls):
        from sqlalchemy import Column, Integer
        return Column(Integer, primary_key=True, index=True)


class CreatedUpdatedMixin:
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now, onupdate=datetime.now
    )