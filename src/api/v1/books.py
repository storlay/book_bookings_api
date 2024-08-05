from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    Query,
    status,
)

from src.api.dependencies import TransactionDep
from src.api.pagination import (
    BasePaginationResponse,
    PaginationParams,
    Paginator,
)
from src.schemas.books import (
    AddBookSchema,
    BookIdSchema,
    BookFiltersSchema,
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
    summary="Get all books",
    description="Get all books with pagination.",
)
async def get_all_books(
    transaction: TransactionDep,
    pagination: PaginationParams = Depends(),
) -> BasePaginationResponse[BookSchema]:
    """
    Getting all books.
    :param transaction: Database transaction.
    :param pagination: Pagination params.
    :return: List of Pydantic models representing the book.
    """
    list_books = await BooksService.get_all_books(
        transaction,
    )
    paginator = Paginator(
        pages=list_books,
        params=pagination,
    )
    return paginator.get_response()


@router.get(
    "/filters",
    status_code=status.HTTP_200_OK,
    summary="Get books by filters",
    description="Get books by filters with pagination.",
)
async def get_books_by_filters(
    transaction: TransactionDep,
    pagination: PaginationParams = Depends(),
    filters: BookFiltersSchema = Depends(),
    genres: list[str] = Query(None)
) -> BasePaginationResponse[BookSchema]:
    """
    Getting a list books by filters.
    :param transaction: Database transaction.
    :param pagination: Pagination params.
    :param filters: Pydantic model representing the search filters.
    :param genres: List of genres.
    :return: List of Pydantic models representing the book.
    """
    list_books = await BooksService.get_books_by_filters(
        transaction,
        filters,
        genres,
    )
    paginator = Paginator(
        pages=list_books,
        params=pagination,
    )
    return paginator.get_response()


@router.get(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Get book by ID",
    description="Get book by ID.",
)
async def get_book(
    transaction: TransactionDep,
    book_id: Annotated[int, Path(ge=1)],
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
    summary="Add one book",
    description="Add one book.",
)
async def add_book(
    transaction: TransactionDep,
    book_data: AddBookSchema = Depends(),
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
    summary="Update book by ID",
    description="Update book by ID.",
)
async def update_book(
    transaction: TransactionDep,
    book_id: Annotated[int, Path(ge=1)],
    genres: list[str] = Query(...),
    book_data: UpdateBookSchema = Depends(),
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
    summary="Delete book by ID",
    description="Delete book by ID.",
)
async def delete_book(
    transaction: TransactionDep,
    book_id: Annotated[int, Path(ge=1)],
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
