from fastapi import (
    APIRouter,
    Query,
    status,
)

from src.api.dependencies import TransactionDep
from src.schemas.books import (
    AddBookSchema,
    BookIdSchema,
    BookSchema,
    UpdateBookSchema,
)
from src.services.books import BooksService

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get(
    "/all",
    status_code=status.HTTP_200_OK,
)
async def get_all_books(
    transaction: TransactionDep,
) -> list[BookSchema]:
    """
    Getting all books.
    :param transaction: Database transaction.
    :return: List of Pydantic models representing the book.
    """
    return await BooksService.get_all_books(
        transaction,
    )


@router.get(
    "/filters",
    status_code=status.HTTP_200_OK,
)
async def get_books_by_filters(
    transaction: TransactionDep,
    author_name: str = Query(None),
    author_surname: str = Query(None),
    genres: list[str] = Query(None),
    min_price: float = Query(None, ge=0),
    max_price: float = Query(None, ge=0),
) -> list[BookSchema]:
    """
    Getting a list books by filters.
    :param transaction: Database transaction.
    :param author_name: Author's name.
    :param author_surname: Author's surname.
    :param genres: List of genres.
    :param min_price: Minimum price.
    :param max_price: Maximum price.
    :return: List of Pydantic models representing the book.
    """
    return await BooksService.get_books_by_filters(
        transaction,
        author_name,
        author_surname,
        genres,
        min_price,
        max_price,
    )


@router.get(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
)
async def get_book(
    transaction: TransactionDep,
    book_id: int,
) -> BookSchema:
    """
    Getting a book by ID.
    :param transaction: Database transaction.
    :param book_id: Book ID.
    :return: Pydantic model representing the book.
    """
    return await BooksService.get_book(
        transaction,
        book_id,
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def add_book(
    transaction: TransactionDep,
    book_data: AddBookSchema,
    genres: list[str] = Query(None),
) -> BookIdSchema:
    """
    Adding a new book.
    :param transaction: Database transaction.
    :param book_data: Pydantic model representing book data.
    :param genres: List of genres.
    :return: Pydantic model representing the created book ID.
    """
    return await BooksService.add_book(
        transaction,
        book_data,
        genres,
    )


@router.put(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
)
async def update_book(
    transaction: TransactionDep,
    book_id: int,
    book_data: UpdateBookSchema,
    genres: list[str],
) -> BookIdSchema:
    """
    Updating a book by ID.
    :param transaction: Database transaction.
    :param book_id: Book ID.
    :param book_data: Pydantic model representing book data.
    :param genres: List of genres.
    :return: Pydantic model representing the updated book ID.
    """
    return await BooksService.update_book(
        transaction,
        book_id,
        book_data,
        genres,
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_book(
    transaction: TransactionDep,
    book_id: int,
) -> None:
    """
    Deleting a book by ID.
    :param transaction: Database transaction.
    :param book_id: Book ID.
    :return: None.
    """
    return await BooksService.delete_book(
        transaction,
        book_id,
    )
