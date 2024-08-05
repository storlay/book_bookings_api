from fastapi import status

from src.exceptions.base import CatalogException


class BookWasNotFoundException(CatalogException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "The book was not found"


class IncorrectAuthorException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Wrong author id"
