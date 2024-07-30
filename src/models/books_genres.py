from sqlalchemy import (
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.db.database import Base


class BooksGenres(Base):
    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "genre_id",
            name="idx_unique_book_genre",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
    )
    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genres.id", ondelete="CASCADE"),
    )
