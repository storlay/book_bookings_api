from fastapi import APIRouter, status

from src.api.dependencies import TransactionDep
from src.schemas.bookings import (
    AddOrUpdateBookingSchema,
    BookingIdSchema,
    BookingSchema,
)
from src.services.bookings import BookingsService

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get(
    "/{booking_id}",
    status_code=status.HTTP_200_OK
)
async def get_booking(
        transaction: TransactionDep,
        booking_id: int
) -> BookingSchema:
    return await BookingsService.get_booking(
        transaction,
        booking_id
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_all_bookings(
        transaction: TransactionDep
) -> list[BookingSchema]:
    return await BookingsService.get_all_bookings(
        transaction
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def add_booking(
        transaction: TransactionDep,
        booking_data: AddOrUpdateBookingSchema
) -> BookingIdSchema:
    return await BookingsService.add_booking(
        transaction,
        booking_data
    )


@router.put(
    "/{booking_id}",
    status_code=status.HTTP_200_OK
)
async def update_booking(
        transaction: TransactionDep,
        booking_id: int,
        booking_data: AddOrUpdateBookingSchema
) -> BookingIdSchema:
    return await BookingsService.update_booking(
        transaction,
        booking_id,
        booking_data
    )


@router.delete(
    "/{booking_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_booking(
        transaction: TransactionDep,
        booking_id: int

) -> None:
    await BookingsService.delete_booking(
        transaction,
        booking_id
    )
