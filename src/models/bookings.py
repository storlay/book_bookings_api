from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.db.database import Base
from src.schemas.bookings import BookingSchema


class Bookings(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
    )
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    def to_read_model(self) -> BookingSchema:
        return BookingSchema(
            id=self.id,
            book_id=self.book_id,
            date_from=self.date_from,
            date_to=self.date_to,
            user_id=self.user_id,
        )
