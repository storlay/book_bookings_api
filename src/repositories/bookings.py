from datetime import date

from sqlalchemy import select, and_, or_, delete

from src.models.bookings import Bookings
from src.utils.repository import BaseRepository


class BookingsRepository(BaseRepository):
    model = Bookings

    async def check_booking(
            self,
            book_id: int,
            date_from: date,
            date_to: date
    ) -> bool | int:
        query = (
            select(self.model.user_id)
            .filter(
                and_(
                    self.model.book_id == book_id,
                    or_(
                        and_(
                            self.model.date_from <= date_from,
                            self.model.date_to >= date_from
                        ),
                        and_(
                            self.model.date_from <= date_to,
                            self.model.date_to >= date_to
                        ),
                        and_(
                            self.model.date_from >= date_from,
                            self.model.date_to <= date_to
                        )
                    )
                )
            )
        )
        is_booked = await self.session.execute(query)
        bookings = is_booked.scalar_one_or_none()
        return bookings

    async def remove_old_bookings(
            self,
            current_date: date
    ) -> None:
        query = (
            delete(Bookings)
            .filter(Bookings.date_to <= current_date)
        )
        await self.session.execute(query)
