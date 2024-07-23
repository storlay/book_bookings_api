from fastapi import HTTPException, status


class CatalogException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal server error"

    def __init__(
            self
    ):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail
        )


class AvatarFileWasNotFoundException(CatalogException):
    detail = "The avatar file was not found"


class AvatarFileIsNotLoadedException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The avatar is not loaded"


class UserWasNotFoundException(CatalogException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The user was not found"
