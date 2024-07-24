from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.db.database import Base

from datetime import datetime

from src.schemas.bookings import BookingSchema


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False
    )
    date_from: Mapped[datetime] = mapped_column(nullable=False)
    date_to: Mapped[datetime] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    def to_read_model(self) -> BookingSchema:
        return BookingSchema(
            id=self.id,
            date_from=self.date_from,
            date_to=self.date_to,
            user_id=self.user_id
        )
