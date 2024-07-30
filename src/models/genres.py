from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.schemas.genres import GenreSchema


class Genres(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    books: Mapped[list["Books"]] = relationship(
        secondary="books_genres",
        back_populates="genres",
        lazy="selectin",
    )

    def to_read_model(self) -> GenreSchema:
        return GenreSchema(
            id=self.id,
            name=self.name,
        )
