from fastapi import status

from src.exceptions.base import CatalogException


class AvatarFileWasNotFoundException(CatalogException):
    detail = "The avatar file was not found"


class AvatarFileIsNotLoadedException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The avatar is not loaded"


class UserWasNotFoundException(CatalogException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "The user was not found"
