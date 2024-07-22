from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.db.database import Base


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE")
    )

    author: Mapped["Users"] = relationship("Users", back_populates="books")
