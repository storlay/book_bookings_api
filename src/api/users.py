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
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
async def get_user(
        transaction: TransactionDep,
        user_id: int
) -> UserSchema:
    return await UsersService.get_user(
        transaction,
        user_id
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_all_users(
        transaction: TransactionDep
) -> list[UserSchema]:
    return await UsersService.get_all_users(
        transaction
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def add_user(
        transaction: TransactionDep,
        user_data: UserInitialsSchema
) -> UserIdSchema:
    return await UsersService.add_user(
        transaction,
        user_data
    )


@router.patch(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
async def update_user_initials(
        transaction: TransactionDep,
        user_id: int,
        fields: UserInitialsSchema
) -> UserIdSchema:
    return await UsersService.update_user(
        transaction,
        user_id,
        fields
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
        transaction: TransactionDep,
        user_id: int
) -> None:
    await UsersService.delete_user(
        transaction,
        user_id
    )


@router.patch(
    "/{user_id}/avatar",
    status_code=status.HTTP_200_OK
)
async def upload_avatar(
        transaction: TransactionDep,
        user_id: int,
        user_avatar: UploadFile
) -> UserIdSchema:
    return await UsersService.upload_avatar(
        transaction,
        user_id,
        user_avatar
    )


@router.delete(
    "/{user_id}/avatar",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_avatar(
        transaction: TransactionDep,
        user_id: int
) -> None:
    await UsersService.delete_avatar(
        transaction,
        user_id
    )
