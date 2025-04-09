from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from .config import config

from redis import asyncio as aioredis

@asynccontextmanager
async def lifespan(_: FastAPI):
    redis = aioredis.from_url(config.REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield
    
app  = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)