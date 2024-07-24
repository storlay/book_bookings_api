from fastapi import status

from src.utils.exception import CatalogException


class BookWasNotFoundException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The book was not found"


class IncorrectAuthorException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Wrong author id"
