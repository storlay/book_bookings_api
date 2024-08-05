from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    status,
)

from src.api.dependencies import TransactionDep
from src.api.pagination import (
    BasePaginationResponse,
    PaginationParams,
    Paginator,
)
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
    summary="Get all bookings",
    description="Get all bookings with pagination.",
)
async def get_all_bookings(
    transaction: TransactionDep,
    pagination: PaginationParams = Depends(),
) -> BasePaginationResponse[BookingSchema]:
    """
    Getting all bookings.
    :param transaction: Database transaction.
    :param pagination: Pagination params.
    :return: List of Pydantic models representing the bookings.
    """
    list_bookings = await BookingsService.get_all_bookings(
        transaction,
    )
    paginator = Paginator(
        pages=list_bookings,
        params=pagination,
    )
    return paginator.get_response()


@router.get(
    "/{booking_id}",
    status_code=status.HTTP_200_OK,
    summary="Get booking by ID",
    description="Get booking by ID.",
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
    summary="Add one booking",
    description="Add one booking."
)
async def add_booking(
    transaction: TransactionDep,
    booking_data: AddBookingSchema = Depends(),
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
    summary="Update booking by ID",
    description="Update booking by ID.",
)
async def update_booking(
    transaction: TransactionDep,
    booking_id: Annotated[int, Path(ge=1)],
    booking_data: UpdateBookingSchema = Depends(),
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
    summary="Delete booking by ID",
    description="Delete booking by ID."
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
