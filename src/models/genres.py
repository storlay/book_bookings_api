from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.models.books_genres import books_genres
from src.schemas.genres import GenreSchema


class Genres(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    books: Mapped[list["Books"]] = relationship(
        back_populates="genres",
        secondary=books_genres,
        lazy="joined"
    )

    def to_read_model(self) -> GenreSchema:
        return GenreSchema(
            id=self.id,
            name=self.name
        )
