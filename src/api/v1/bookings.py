from typing import Annotated

from fastapi import (
    APIRouter,
    Path,
    status,
)

from src.api.dependencies import TransactionDep
from src.schemas.bookings import (
    AddBookingSchema,
    BookingIdSchema,
    BookingSchema,
    UpdateBookingSchema,
)
from src.services.bookings import BookingsService

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get(
    "/all",
    status_code=status.HTTP_200_OK,
)
async def get_all_bookings(
    transaction: TransactionDep,
) -> list[BookingSchema]:
    """
    Getting all bookings.
    :param transaction: Database transaction.
    :return: List of Pydantic models representing the bookings.
    """
    return await BookingsService.get_all_bookings(
        transaction,
    )


@router.get(
    "/{booking_id}",
    status_code=status.HTTP_200_OK,
)
async def get_booking(
    transaction: TransactionDep,
    booking_id: Annotated[int, Path(ge=1)],
) -> BookingSchema:
    """
    Getting a booking by ID.
    :param transaction: Database transaction.
    :param booking_id: Booking ID.
    :return: Pydantic model representing the booking.
    """
    return await BookingsService.get_booking(
        transaction,
        booking_id,
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def add_booking(
    transaction: TransactionDep,
    booking_data: AddBookingSchema,
) -> BookingIdSchema:
    """
    Adding a new booking.
    :param transaction: Database transaction.
    :param booking_data: Pydantic model representing booking data.
    :return: Pydantic model representing the created booking ID.
    """
    return await BookingsService.add_booking(
        transaction,
        booking_data,
    )


@router.put(
    "/{booking_id}",
    status_code=status.HTTP_200_OK,
)
async def update_booking(
    transaction: TransactionDep,
    booking_id: Annotated[int, Path(ge=1)],
    booking_data: UpdateBookingSchema,
) -> BookingIdSchema:
    """
    Updating a booking by ID.
    :param transaction: Database transaction.
    :param booking_id: Booking ID.
    :param booking_data: Pydantic model representing booking data.
    :return: Pydantic model representing the updated booking ID.
    """
    return await BookingsService.update_booking(
        transaction,
        booking_id,
        booking_data,
    )


@router.delete(
    "/{booking_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_booking(
    transaction: TransactionDep,
    booking_id: Annotated[int, Path(ge=1)],
) -> None:
    """
    Deleting a booking by ID.
    :param transaction: Database transaction.
    :param booking_id: Booking ID.
    :return: None.
    """
    await BookingsService.delete_booking(
        transaction,
        booking_id,
    )
