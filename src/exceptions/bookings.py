from fastapi import status

from src.utils.exception import CatalogException


class BookingWasNotFoundException(CatalogException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "The booking was not found"


class BookIsBookedException(CatalogException):
    status_code = status.HTTP_409_CONFLICT
    detail = "The book has already been booked for the selected dates"


class DateFromCannotBeAfterDateToException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The start date cannot be later than the end date"


class InvalidUserOrBookDataException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid user or book data"
