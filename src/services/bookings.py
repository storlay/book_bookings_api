from sqlalchemy.exc import NoResultFound

from src.exceptions.bookings import (
    BookingWasNotFoundException,
    BookIsBookedException,
    DateFromCannotBeAfterDateToException,
    InvalidUserOrBookDataException,
)
from src.schemas.bookings import (
    AddBookingSchema,
    BookingIdSchema,
    BookingSchema,
    UpdateBookingSchema,
)
from src.utils.transaction import BaseManager


class BookingsService:
    @staticmethod
    async def get_booking(
        transaction: BaseManager,
        booking_id: int,
    ) -> BookingSchema:
        """
        The logic of getting a booking.
        :param transaction: Database transaction.
        :param booking_id: Booking ID
        :return: Pydantic model representing the booking.
        """
        async with transaction:
            try:
                booking = await transaction.bookings_repo.find_one(
                    id=booking_id,
                )
                return booking
            except NoResultFound:
                raise BookingWasNotFoundException

    @staticmethod
    async def get_all_bookings(
        transaction: BaseManager,
    ) -> list[BookingSchema]:
        """
        The logic of receiving all bookings.
        :param transaction: Database transaction.
        :return: List of Pydantic models representing the bookings.
        """
        async with transaction:
            bookings = await transaction.bookings_repo.find_all()
            return bookings

    @classmethod
    async def add_booking(
        cls,
        transaction: BaseManager,
        booking_data: AddBookingSchema,
    ) -> BookingIdSchema:
        """
        The logic of creating a booking.
        :param transaction: Database transaction.
        :param booking_data: Pydantic model representing booking data.
        :return: Pydantic model representing the created booking ID.
        """
        async with transaction:
            is_booked = await cls.validate_booking_data(
                transaction,
                booking_data,
            )

            if is_booked:
                raise BookIsBookedException
            booking_id = await transaction.bookings_repo.add_one(
                booking_data.model_dump(),
            )
            await transaction.commit()
            return BookingIdSchema(booking_id=booking_id)

    @classmethod
    async def update_booking(
        cls,
        transaction: BaseManager,
        booking_id: int,
        booking_data: UpdateBookingSchema,
    ) -> BookingIdSchema:
        """
        The logic of updating a booking by ID
        :param transaction: Database transaction.
        :param booking_id: Booking ID.
        :param booking_data: Pydantic model representing booking data.
        :return: Pydantic model representing the updated booking ID.
        """
        async with transaction:
            is_booked = await cls.validate_booking_data(
                transaction,
                booking_data,
            )
            if is_booked and is_booked != booking_data.user_id:
                raise BookIsBookedException

            booking_data_dict = booking_data.model_dump()
            await transaction.bookings_repo.edit_one(
                obj_id=booking_id,
                data=booking_data_dict,
            )
            await transaction.commit()
            return BookingIdSchema(booking_id=booking_id)

    @staticmethod
    async def delete_booking(
        transaction: BaseManager,
        booking_id: int,
    ) -> None:
        """
        The logic of deleting a booking by ID
        :param transaction: Database transaction.
        :param booking_id: Booking ID
        :return: None.
        """
        async with transaction:
            try:
                await transaction.bookings_repo.find_one(
                    id=booking_id,
                )
            except NoResultFound:
                raise BookingWasNotFoundException

            await transaction.bookings_repo.delete_one(
                obj_id=booking_id,
            )
            await transaction.commit()

    @staticmethod
    async def validate_booking_data(
        transaction: BaseManager,
        booking_data: AddBookingSchema | UpdateBookingSchema,
    ) -> int | bool:
        """
        Validation of booking data.
        :param transaction: Database transaction.
        :param booking_data: Pydantic model representing booking data.
        :return: User ID if the data has been verified
                 and None if not.
        """
        if booking_data.date_from > booking_data.date_to:
            raise DateFromCannotBeAfterDateToException

        async with transaction:
            try:
                await transaction.users_repo.find_one(
                    id=booking_data.user_id,
                )
                await transaction.books_repo.find_one(
                    id=booking_data.book_id,
                )
            except NoResultFound:
                raise InvalidUserOrBookDataException

            is_booked = await transaction.bookings_repo.check_booking(
                booking_data.book_id,
                booking_data.date_from,
                booking_data.date_to,
            )
            return is_booked
