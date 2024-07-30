from sqlalchemy.exc import (
    IntegrityError,
    NoResultFound,
)

from src.exceptions.books import (
    BookWasNotFoundException,
    IncorrectAuthorException,
)
from src.schemas.books import (
    AddBookSchema,
    BookIdSchema,
    BookSchema,
    UpdateBookSchema,
)
from src.utils.transaction import BaseManager


class BooksService:
    @staticmethod
    async def get_book(
        transaction: BaseManager,
        book_id: int,
    ) -> BookSchema:
        """
        The logic of getting a book by ID.
        :param transaction: Database transaction.
        :param book_id: Book ID.
        :return: Pydantic model representing the book.
        """
        try:
            async with transaction:
                book = await transaction.books_repo.find_one(
                    id=book_id,
                )
                return book
        except NoResultFound:
            raise BookWasNotFoundException

    @staticmethod
    async def get_all_books(
        transaction: BaseManager,
    ) -> list[BookSchema]:
        """
        The logic of getting all the books.
        :param transaction: Database transaction.
        :return: List of Pydantic models representing the book.
        """
        async with transaction:
            books = await transaction.books_repo.find_all()
            return books

    @staticmethod
    async def add_book(
        transaction: BaseManager,
        book_data: AddBookSchema,
        genres: list[str],
    ) -> BookIdSchema:
        """
        The logic of adding a book.
        :param transaction: Database transaction.
        :param book_data: Pydantic model representing book data.
        :param genres: List of genres.
        :return: Pydantic model representing the created book ID.
        """
        book_data_dict = book_data.model_dump()
        async with transaction:
            new_book = await transaction.books_repo.add_one(
                book_data_dict,
            )
            genres = await transaction.genres_repo.find_by_names(
                genres,
            )
            new_book.genres = genres
            await transaction.commit()
            return BookIdSchema(book_id=new_book.id)

    @staticmethod
    async def update_book(
        transaction: BaseManager,
        book_id: int,
        book_data: UpdateBookSchema,
        genres: list[str],
    ) -> BookIdSchema:
        """
        The logic of updating a book by ID.
        :param transaction: Database transaction.
        :param book_id: Book ID.
        :param book_data: Pydantic model representing book data.
        :param genres: List of genres.
        :return: Pydantic model representing the updated book ID.
        """
        book_data_dict = book_data.model_dump()
        try:
            async with transaction:
                book = await transaction.books_repo.edit_one(
                    obj_id=book_id,
                    data=book_data_dict,
                )
                genres = await transaction.genres_repo.find_by_names(
                    genres,
                )
                book.genres = genres
                await transaction.commit()
                return BookIdSchema(book_id=book_id)
        except NoResultFound:
            raise BookWasNotFoundException
        except IntegrityError:
            raise IncorrectAuthorException

    @staticmethod
    async def delete_book(
        transaction: BaseManager,
        book_id: int,
    ) -> None:
        """
        The logic of deleting a book by ID.
        :param transaction: Database transaction.
        :param book_id: Book ID
        :return: None.
        """
        async with transaction:
            try:
                await transaction.books_repo.find_one(
                    id=book_id,
                )
            except NoResultFound:
                raise BookWasNotFoundException

            await transaction.books_repo.delete_one(
                obj_id=book_id,
            )
            await transaction.commit()

    @staticmethod
    async def get_books_by_filters(
        transaction: BaseManager,
        author_name: str | None,
        author_surname: str | None,
        genres: list[str] | None,
        min_price: float | None,
        max_price: float | None,
    ) -> list[BookSchema | None]:
        """
        The logic of getting
        a list of books by filters.
        :param transaction: Database transaction.
        :param author_name: Author's name.
        :param author_surname: Author's surname.
        :param genres: List of genres.
        :param min_price: Minimum price.
        :param max_price: Maximum price.
        :return: List of Pydantic models representing the book.
        """
        async with transaction:
            books = await transaction.books_repo.find_with_filters(
                author_name,
                author_surname,
                genres,
                min_price,
                max_price,
            )
            return books
