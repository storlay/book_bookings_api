from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base


class Genres(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    books: Mapped["Books"] = relationship("Books", back_populates="genres")
