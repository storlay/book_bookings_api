from datetime import date

from sqlalchemy import (
    and_,
    delete,
    or_,
    select,
)

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
        """
        Checking the availability
        of the book on the requested dates
        :param book_id: Book ID.
        :param date_from: Booking start date.
        :param date_to: Booking end date.
        :return: User ID if the book is busy
                 and None if not.
        """
        statement = (
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
        is_booked = await self.session.execute(statement)
        bookings = is_booked.scalar_one_or_none()
        return bookings

    async def remove_old_bookings(
            self,
            current_date: date
    ) -> None:
        """
        Deleting bookings
        with an expired end date
        :param current_date: Current date
        :return: None.
        """
        query = (
            delete(self.model)
            .filter(self.model.date_to <= current_date)
        )
        await self.session.execute(query)
