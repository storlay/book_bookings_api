from sqlalchemy import ForeignKey, Table
from sqlalchemy.testing.schema import Column

from src.db.database import Base

books_genres = Table(
    "books_genres",
    Base.metadata,
    Column('book_id', ForeignKey("books.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
)
