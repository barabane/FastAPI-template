from abc import ABC
from typing import List

from pydantic import BaseModel
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Base


class AbstractRepository(ABC):
    def __init__(self, session: AsyncSession, model):
        self._session: AsyncSession = session
        self._model: Base = model

    async def get_by_id(self, id) -> Base | None:
        return await self._session.get(entity=self._model, ident=id)

    async def get_all(self, filters: dict = {}) -> List[Base]:
        offset = filters.get("offset") or 0
        limit = filters.get("limit") or 10
        order_by = filters.get("order_by") or None

        return (
            (
                await self._session.execute(
                    select(self._model)
                    .filter_by(**filters)
                    .offset(offset=offset)
                    .limit(limit=limit)
                    .order_by(order_by)
                )
            )
            .scalars()
            .all()
        )

    async def add(self, entity: BaseModel) -> Base:
        return (
            await self._session.execute(
                insert(self._model).values(**entity.model_dump()).returning(self._model)
            )
        ).scalar_one()

    async def add_many(self, entities: List[BaseModel]) -> List[Base]:
        return (
            (
                await self._session.execute(
                    insert(self._model)
                    .values([entity.model_dump() for entity in entities])
                    .returning(self._model)
                )
            )
            .scalars()
            .all()
        )

    async def update(self, id, new_entity: BaseModel) -> Base:
        return (
            await self._session.execute(
                update(self._model)
                .values(**new_entity.model_dump())
                .where(self._model.id == id)
                .returning(self._model)
            )
        ).scalar_one()

    async def delete_by_id(self, id):
        await self._repository.delete(id=id)
