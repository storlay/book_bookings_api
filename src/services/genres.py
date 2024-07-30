from sqlalchemy.exc import (
    IntegrityError,
    NoResultFound,
)

from src.exceptions.genres import (
    DuplicatedGenreException,
    GenreWasNotFoundException,
)
from src.schemas.genres import (
    AddGenreSchema,
    GenreIdSchema,
    GenreSchema,
    UpdateGenreSchema,
)
from src.utils.transaction import BaseManager


class GenresService:
    @staticmethod
    async def get_genre(
        transaction: BaseManager,
        genre_id: int,
    ) -> GenreSchema:
        """
        The logic of getting a genre by ID.
        :param transaction: Database transaction.
        :param genre_id: Genre ID.
        :return: Pydantic model representing the genre.
        """
        try:
            async with transaction:
                genre = await transaction.genres_repo.find_one(
                    id=genre_id,
                )
                return genre
        except NoResultFound:
            raise GenreWasNotFoundException

    @staticmethod
    async def get_all_genres(
        transaction: BaseManager,
    ) -> list[GenreSchema]:
        """
        The logic of getting a list of genres.
        :param transaction: Database transaction.
        :return: List of Pydantic models representing the genre.
        """
        async with transaction:
            genres = await transaction.genres_repo.find_all()
            return genres

    @staticmethod
    async def add_genre(
        transaction: BaseManager,
        genre_data: AddGenreSchema,
    ) -> GenreIdSchema:
        """
        The logic of adding a genre.
        :param transaction: Database transaction.
        :param genre_data: Pydantic model representing genre data.
        :return: Pydantic model representing the created genre ID.
        """
        genre_data_dict = genre_data.model_dump()
        try:
            async with transaction:
                genre_id = await transaction.genres_repo.add_one(
                    genre_data_dict,
                )
                await transaction.commit()
                return GenreIdSchema(
                    genre_id=genre_id,
                )
        except IntegrityError:
            raise DuplicatedGenreException

    @staticmethod
    async def update_genre(
        transaction: BaseManager,
        genre_id: int,
        genre_data: UpdateGenreSchema,
    ) -> GenreIdSchema:
        """
        The logic of updating the genre by ID.
        :param transaction: Database transaction.
        :param genre_id: Genre ID
        :param genre_data: Pydantic model representing genre data.
        :return: Pydantic model representing the updated genre ID.
        """
        try:
            async with transaction:
                await transaction.genres_repo.edit_one(
                    obj_id=genre_id,
                    data={"name": genre_data.name},
                )
                await transaction.commit()
                return GenreIdSchema(
                    genre_id=genre_id,
                )
        except NoResultFound:
            raise GenreWasNotFoundException
        except IntegrityError:
            raise DuplicatedGenreException

    @staticmethod
    async def delete_genre(
        transaction: BaseManager,
        genre_id: int,
    ) -> None:
        """
        The logic of deleting a genre by ID.
        :param transaction: Database transaction.
        :param genre_id: Genre ID.
        :return: None.
        """
        async with transaction:
            try:
                await transaction.genres_repo.find_one(
                    id=genre_id,
                )
            except NoResultFound:
                raise GenreWasNotFoundException

            await transaction.genres_repo.delete_one(
                genre_id,
            )
            await transaction.commit()
