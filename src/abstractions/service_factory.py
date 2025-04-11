from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Base
from .repository import AbstractRepository
from .service import AbstractService


class AbstractServiceFactory(ABC):
    def __init__(
        self,
        service: type[AbstractService],
        repository: type[AbstractRepository],
        model: type[Base],
    ):
        self._service: type[AbstractService] = service
        self._repository: type[AbstractRepository] = repository
        self._model: type[Base] = model

    async def create_repository(self, session):
        return self._repository(session=session, model=self._model)

    async def create_service(self, session: AsyncSession) -> AbstractService:
        return self._service(
            repository=self._repository(session=session, model=self._model)
        )
