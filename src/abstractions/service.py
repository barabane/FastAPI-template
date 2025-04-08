from abc import ABC
from typing import List

from pydantic import BaseModel

from .repository import AbstractRepository


class AbstractService(ABC):
    def __init__(self, repository: AbstractRepository):
        self._repository: AbstractRepository = repository

    async def get_by_id(self, id):
        return await self._repository.get_by_id(id=id)

    async def get_all(self, filters: dict = {}, query_parameters: dict = {}):
        filters = {**filters, **query_parameters}
        return await self._repository.get_all(filters=filters)

    async def add(self, entity: BaseModel):
        return await self._repository.add(entity=entity)

    async def add_many(self, entities: List[BaseModel]):
        return await self._repository.add_many(entities=entities)

    async def update(self, id, new_entity: BaseModel):
        return await self._repository.update(id=id, new_entity=new_entity)

    async def delete_by_id(self, id):
        await self._repository.delete_by_id(id=id)
