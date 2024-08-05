import os

from fastapi import UploadFile
from sqlalchemy.exc import NoResultFound

from src.exceptions.users import (
    AvatarFileIsNotLoadedException,
    AvatarFileWasNotFoundException,
    UserWasNotFoundException,
)
from src.schemas.users import (
    UserIdSchema,
    UserInitialsSchema,
    UserSchema,
)
from src.config.config import settings
from src.utils.transaction import BaseManager


class UsersService:
    @staticmethod
    async def get_user(
        transaction: BaseManager,
        user_id: int,
    ) -> UserSchema:
        """
        The logic of getting a user by ID.
        :param transaction: Database transaction.
        :param user_id: User ID.
        :return: Pydantic model representing the user.
        """
        try:
            async with transaction:
                user = await transaction.users_repo.find_one(
                    id=user_id,
                )
                return user
        except NoResultFound:
            raise UserWasNotFoundException

    @staticmethod
    async def get_all_users(
        transaction: BaseManager,
    ) -> list[UserSchema]:
        async with transaction:
            users = await transaction.users_repo.find_all()
            return users

    @staticmethod
    async def add_user(
        transaction: BaseManager,
        user_data: UserInitialsSchema,
    ) -> UserIdSchema:
        """
        The logic of creating a user.
        :param transaction: Database transaction.
        :param user_data: Pydantic model representing user data.
        :return: Pydantic model representing the created user ID.
        """
        user_dict = user_data.model_dump()
        async with transaction:
            user_id = await transaction.users_repo.add_one(
                user_dict,
            )
            await transaction.commit()
            return UserIdSchema(user_id=user_id)

    @staticmethod
    async def update_user(
        transaction: BaseManager,
        user_id: int,
        fields: UserInitialsSchema,
    ) -> UserIdSchema:
        """
        The logic of updating a user initials by ID.
        :param transaction: Database transaction.
        :param user_id: User ID.
        :param fields: Pydantic model representing fields.
        :return: Pydantic model representing the updated user ID.
        """
        fields_dict = fields.model_dump()
        try:
            async with transaction:
                user_id = await transaction.users_repo.edit_one(
                    obj_id=user_id,
                    data=fields_dict,
                )
                await transaction.commit()
                return UserIdSchema(user_id=user_id)
        except NoResultFound:
            raise UserWasNotFoundException

    @staticmethod
    async def delete_user(
        transaction: BaseManager,
        user_id: int,
    ) -> None:
        """
        The logic of deleting a user by ID.
        :param transaction: Database transaction.
        :param user_id: User ID.
        :return: None.
        """
        try:
            async with transaction:
                user = await transaction.users_repo.find_one(
                    id=user_id,
                )
                if user.avatar_path:
                    os.remove(user.avatar_path)
                await transaction.users_repo.delete_one(
                    user_id,
                )
                await transaction.commit()
        except NoResultFound:
            raise UserWasNotFoundException

    @staticmethod
    async def upload_avatar(
        transaction: BaseManager,
        user_id: int,
        user_avatar: UploadFile,
    ) -> UserIdSchema:
        """
        The logic of uploading the user's avatar.
        :param transaction: Database transaction.
        :param user_id: User ID.
        :param user_avatar: User avatar.
        :return: Pydantic model representing the updated user ID.
        """
        try:
            async with transaction:
                await transaction.users_repo.find_one(
                    id=user_id,
                )
        except NoResultFound:
            raise NoResultFound

        avatar_filename = f"{user_id}.jpg"
        avatar_path = settings.user.AVATAR_PATH + avatar_filename
        with open(avatar_path, "wb") as buffer:
            buffer.write(await user_avatar.read())

            async with transaction:
                user_id = await transaction.users_repo.edit_one(
                    obj_id=user_id,
                    data={"avatar_path": avatar_path},
                )
                await transaction.commit()
                return UserIdSchema(user_id=user_id)

    @staticmethod
    async def delete_avatar(
        transaction: BaseManager,
        user_id: int,
    ) -> None:
        """
        The logic of deleting a user's avatar.
        :param transaction: Database transaction.
        :param user_id: User ID.
        :return: None.
        """
        try:
            async with transaction:
                user = await transaction.users_repo.find_one(
                    id=user_id,
                )
                if user.avatar_path:

                    try:
                        os.remove(user.avatar_path)
                    except FileNotFoundError:
                        raise AvatarFileWasNotFoundException

                    await transaction.users_repo.edit_one(
                        obj_id=user_id,
                        data={"avatar_path": None},
                    )
                    await transaction.commit()
                else:
                    raise AvatarFileIsNotLoadedException
        except NoResultFound:
            raise UserWasNotFoundException
