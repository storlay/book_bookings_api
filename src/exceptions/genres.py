from fastapi import status

from src.utils.exception import CatalogException


class GenreWasNotFoundException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The genre was not found"


class DuplicatedGenreException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "A genre with that name already exists"


class IncorrectNamesOfGenreException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Incorrect genre names"
