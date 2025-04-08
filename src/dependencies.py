from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import session_maker

async def get_session():
    async with session_maker() as session:
        yield session
        await session.commit()

Session = Annotated[AsyncSession, Depends(get_session)]