from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base
from src.schemas.books import BookSchema


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genres.id", ondelete="SET NULL")
    )

    author: Mapped["Users"] = relationship("Users", back_populates="books")
    genres: Mapped["Genres"] = relationship("Genres", back_populates="books")

    def to_read_model(self) -> BookSchema:
        return BookSchema(
            id=self.id,
            name=self.name,
            price=self.price,
            author_id=self.author_id,
            genre_id=self.genre_id
        )
