from typing import Optional

from fastapi import APIRouter, Query, status

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
    tags=["Books"]
)


@router.get(
    "/{book_id}",
    status_code=status.HTTP_200_OK
)
async def get_book(
        transaction: TransactionDep,
        book_id: int
) -> BookSchema:
    return await BooksService.get_book(
        transaction,
        book_id
    )


@router.get(
    "/all",
    status_code=status.HTTP_200_OK
)
async def get_all_books(
        transaction: TransactionDep
):
    return await BooksService.get_all_books(
        transaction
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def add_book(
        transaction: TransactionDep,
        book_data: AddBookSchema,
        genres: list[str] = Query()
) -> BookIdSchema:
    return await BooksService.add_book(
        transaction,
        book_data,
        genres
    )


@router.put(
    "/{book_id}",
    status_code=status.HTTP_200_OK
)
async def update_book(
        transaction: TransactionDep,
        book_id: int,
        book_data: UpdateBookSchema,
        genres: list[str] = Query()
) -> BookIdSchema:
    return await BooksService.update_book(
        transaction,
        book_id,
        book_data,
        genres
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_200_OK
)
async def delete_book(
        transaction: TransactionDep,
        book_id: int
) -> None:
    return await BooksService.delete_book(
        transaction,
        book_id
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_books_by_filters(
        transaction: TransactionDep,
        author_name: Optional[str] = None,
        author_surname: Optional[str] = None,
        genres: list[str] = Query(None),
        min_price: Optional[float] = Query(None, ge=0),
        max_price: Optional[float] = Query(None, ge=0)
) -> list[BookSchema]:
    return await BooksService.get_books_by_filters(
        transaction,
        author_name,
        author_surname,
        genres,
        min_price,
        max_price
    )
