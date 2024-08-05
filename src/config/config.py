import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    USER: str = os.getenv("POSTGRES_USER")
    PASS: str = os.getenv("POSTGRES_PASSWORD")
    NAME: str = os.getenv("POSTGRES_DB")
    HOST: str = os.getenv("DB_HOST")
    PORT: int = os.getenv("DB_PORT")
    URL: str = f"postgresql+asyncpg://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"


class RedisSettings(BaseModel):
    HOST: str = os.getenv("REDIS_HOST")
    PORT: int = os.getenv("REDIS_PORT")


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()


settings = Settings()
