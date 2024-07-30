from typing import Optional

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.schemas.users import UserSchema


class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    avatar_path: Mapped[Optional[str]]

    books: Mapped["Books"] = relationship(
        "Books",
        back_populates="author",
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            avatar_path=self.avatar_path,
        )
