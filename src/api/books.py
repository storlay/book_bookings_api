from src.api.dependencies import TransactionDep

from fastapi import APIRouter, status

from src.schemas.books import BookSchema, AddBookSchema, BookIdSchema, UpdateBookSchema
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
    "",
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
        book_data: AddBookSchema
) -> BookIdSchema:
    return await BooksService.add_book(
        transaction,
        book_data
    )


@router.put(
    "/{book_id}",
    status_code=status.HTTP_200_OK
)
async def update_book(
        transaction: TransactionDep,
        book_id: int,
        book_data: UpdateBookSchema
) -> BookIdSchema:
    return await BooksService.update_book(
        transaction,
        book_id,
        book_data
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
