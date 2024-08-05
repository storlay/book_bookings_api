import re

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)

from src.config.config import settings


engine = create_async_engine(settings.db.URL)
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        """
        Converting a class name (CamelCase)
        to a table name (snake_case).
        :return: Table Name.
        """
        name = re.sub(
            r"(?<!^)(?=[A-Z])",
            "_",
            cls.__name__,
        ).lower()
        return name
