from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    status,
    UploadFile,
)

from src.api.dependencies import TransactionDep
from src.api.pagination import (
    BasePaginationResponse,
    PaginationParams,
    Paginator,
)
from src.schemas.users import (
    UserIdSchema,
    UserInitialsSchema,
    UserSchema,
)
from src.services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/all",
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    description="Get all users with pagination.",
)
async def get_all_users(
    transaction: TransactionDep,
    pagination: PaginationParams = Depends(),
) -> BasePaginationResponse[UserSchema]:
    """
    Getting all users.
    :param transaction: Database transaction.
    :param pagination: Pagination params.
    :return: List of Pydantic models representing the user.
    """
    list_users = await UsersService.get_all_users(
        transaction,
    )
    paginator = Paginator(
        pages=list_users,
        params=pagination,
    )
    return paginator.get_response()


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Get user by ID",
    description="Get user by ID.",
)
async def get_user(
    transaction: TransactionDep,
    user_id: Annotated[int, Path(ge=1)],
) -> UserSchema:
    """
    Getting a user by ID.
    :param transaction: Database transaction.
    :param user_id: User ID.
    :return: Pydantic model representing the user.
    """
    return await UsersService.get_user(
        transaction,
        user_id,
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Add one user",
    description="Add one user.",
)
async def add_user(
    transaction: TransactionDep,
    user_data: UserInitialsSchema,
) -> UserIdSchema:
    """
    Adding a new user.
    :param transaction: Database transaction.
    :param user_data: Pydantic model representing user data.
    :return: Pydantic model representing the created user ID.
    """
    return await UsersService.add_user(
        transaction,
        user_data,
    )


@router.patch(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Update user initials",
    description="Update user initials (first name, last name).",
)
async def update_user_initials(
    transaction: TransactionDep,
    user_id: Annotated[int, Path(ge=1)],
    fields: UserInitialsSchema,
) -> UserIdSchema:
    """
    Updating a user initials by ID.
    :param transaction: Database transaction.
    :param user_id: User ID.
    :param fields: Pydantic model representing fields.
    :return: Pydantic model representing the updated user ID.
    """
    return await UsersService.update_user(
        transaction,
        user_id,
        fields,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user by ID",
    description="Delete user by ID.",
)
async def delete_user(
    transaction: TransactionDep,
    user_id: Annotated[int, Path(ge=1)],
) -> None:
    """
    Deleting a user by ID.
    :param transaction: Database transaction.
    :param user_id: User ID.
    :return: None.
    """
    await UsersService.delete_user(
        transaction,
        user_id,
    )


@router.patch(
    "/{user_id}/avatar",
    status_code=status.HTTP_200_OK,
    summary="Update user avatar",
    description="Update user avatar by user ID.",

)
async def upload_avatar(
    transaction: TransactionDep,
    user_id: Annotated[int, Path(ge=1)],
    user_avatar: UploadFile,
) -> UserIdSchema:
    """
    Uploading user avatar
    :param transaction: Database transaction.
    :param user_id: User ID.
    :param user_avatar: User avatar.
    :return: Pydantic model representing the updated user ID.
    """
    return await UsersService.upload_avatar(
        transaction,
        user_id,
        user_avatar,
    )


@router.delete(
    "/{user_id}/avatar",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user avatar",
    description="Delete user avatar by user ID.",
)
async def delete_avatar(
    transaction: TransactionDep,
    user_id: Annotated[int, Path(ge=1)],
) -> None:
    """
    Deleting User avatar
    :param transaction: Database transaction.
    :param user_id: User ID.
    :return: None.
    """
    await UsersService.delete_avatar(
        transaction,
        user_id,
    )
