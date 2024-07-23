from src.exceptions.books import BookWasNotFoundException, IncorrectAuthorOrGenreException
from src.schemas.books import BookSchema, AddBookSchema, BookIdSchema, UpdateBookSchema
from src.utils.transaction import BaseManager

from sqlalchemy.exc import NoResultFound, IntegrityError


class BooksService:
    @staticmethod
    async def get_book(
            transaction: BaseManager,
            book_id: int
    ) -> BookSchema:
        try:
            async with transaction:
                book = await transaction.books_repo.find_one(
                    id=book_id
                )
                return book
        except NoResultFound:
            raise BookWasNotFoundException

    @staticmethod
    async def get_all_books(
            transaction: BaseManager
    ):
        async with transaction:
            books = await transaction.books_repo.find_all()
            return books

    @staticmethod
    async def add_book(
            transaction: BaseManager,
            book_data: AddBookSchema
    ) -> BookIdSchema:
        book_data_dict = book_data.model_dump()
        async with transaction:
            book_id = await transaction.books_repo.add_one(
                data=book_data_dict
            )
            await transaction.commit()
            return BookIdSchema(book_id=book_id)

    @staticmethod
    async def update_book(
            transaction: BaseManager,
            book_id: int,
            book_data: UpdateBookSchema
    ) -> BookIdSchema:
        book_data_dict = book_data.model_dump()
        try:
            async with transaction:
                await transaction.books_repo.edit_one(
                    obj_id=book_id,
                    data=book_data_dict
                )
                await transaction.commit()
                return BookIdSchema(book_id=book_id)
        except NoResultFound:
            raise BookWasNotFoundException
        except IntegrityError:
            raise IncorrectAuthorOrGenreException

    @staticmethod
    async def delete_book(
            transaction: BaseManager,
            book_id: int
    ) -> None:
        async with transaction:
            try:
                await transaction.books_repo.find_one(
                    id=book_id
                )
            except NoResultFound:
                raise BookWasNotFoundException

            await transaction.books_repo.delete_one(
                obj_id=book_id
            )
            await transaction.commit()
