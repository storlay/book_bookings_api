from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.schemas.books import BookSchema


class Books(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    author: Mapped["Users"] = relationship(
        "Users",
        back_populates="books",
    )
    genres: Mapped[list["Genres"]] = relationship(
        secondary="books_genres",
        back_populates="books",
        lazy="selectin",
    )

    def to_read_model(self) -> BookSchema:
        return BookSchema(
            id=self.id,
            name=self.name,
            price=self.price,
            author_id=self.author_id,
            genres=[genre.name for genre in self.genres],
        )
