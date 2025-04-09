from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.example")

    PG_HOST: str
    PG_PORT: int
    PG_DB_NAME: str
    PG_USER: str
    PG_PASSWORD: str
    
    REDIS_HOST: str
    REDIS_PORT: int

    API_VERSION: str = "/v1"
    
    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    @property
    def DB_URL(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                host=self.PG_HOST,
                port=self.PG_PORT,
                username=self.PG_USER,
                password=self.PG_PASSWORD,
                path=self.PG_DB_NAME,
            )
        )


config = Config()
