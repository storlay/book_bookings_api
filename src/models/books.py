from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.models.books_genres import books_genres
from src.schemas.books import BookSchema


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    author: Mapped["Users"] = relationship("Users", back_populates="books")
    genres: Mapped[list["Genres"]] = relationship(
        back_populates="books",
        secondary=books_genres,
        lazy="selectin"
    )

    def to_read_model(self) -> BookSchema:
        return BookSchema(
            id=self.id,
            name=self.name,
            price=self.price,
            author_id=self.author_id,
            genres=[genre.name for genre in self.genres]
        )
