from datetime import date

from pydantic import BaseModel


class BookingSchema(BaseModel):
    id: int
    book_id: int
    user_id: int
    date_from: date
    date_to: date


class BookingIdSchema(BaseModel):
    booking_id: int


class AddOrUpdateBookingSchema(BaseModel):
    book_id: int
    user_id: int
    date_from: date
    date_to: date
