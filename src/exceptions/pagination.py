from fastapi import status

from src.exceptions.base import CatalogException


class PageNotFoundException(CatalogException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Page not found"
