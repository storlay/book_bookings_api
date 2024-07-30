from fastapi import (
    APIRouter,
    UploadFile,
    status,
)

from src.api.dependencies import TransactionDep
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
)
async def get_all_users(
    transaction: TransactionDep,
) -> list[UserSchema]:
    """
    Getting all users.
    :param transaction: Database transaction.
    :return: List of Pydantic models representing the user.
    """
    return await UsersService.get_all_users(
        transaction,
    )


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def get_user(
    transaction: TransactionDep,
    user_id: int,
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
)
async def update_user_initials(
    transaction: TransactionDep,
    user_id: int,
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
)
async def delete_user(
    transaction: TransactionDep,
    user_id: int,
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
)
async def upload_avatar(
    transaction: TransactionDep,
    user_id: int,
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
)
async def delete_avatar(
    transaction: TransactionDep,
    user_id: int,
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
