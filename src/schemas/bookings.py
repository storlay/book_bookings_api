from pydantic import BaseModel

from src.schemas.mixins.bookings import (
    DateMixin,
    RelationMixin,
)


class BookingIdSchema(BaseModel):
    booking_id: int


class BookingSchema(
    DateMixin,
    RelationMixin,
):
    id: int


class AddBookingSchema(
    DateMixin,
    RelationMixin,
):
    pass


class UpdateBookingSchema(
    DateMixin,
    RelationMixin,
):
    pass
