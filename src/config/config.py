import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    V1_PREFIX: str = "/v1"


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


class UsersSettings(BaseModel):
    AVATAR_PATH: str = "src/static/users_avatars/"


class Settings(BaseSettings):
    api: ApiSettings = ApiSettings()
    db: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    user: UsersSettings = UsersSettings()


settings = Settings()
