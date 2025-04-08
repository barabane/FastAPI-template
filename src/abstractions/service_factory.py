from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Base
from .repository import AbstractRepository
from .service import AbstractService


class AbstractServiceFactory(ABC):
    def __init__(self, service: AbstractService, repository: AbstractRepository, model: Base):
        self._service: AbstractService = service
        self._repository: AbstractRepository = repository
        self._model: Base = model

    async def create_repository(self, session):
        return self._repository(session=session, model=self._model)

    async def create_service(self, session: AsyncSession) -> AbstractService:
        return self._service(
            repository=self._repository(session=session, model=self._model)
        )
