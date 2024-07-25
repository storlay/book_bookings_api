from fastapi import APIRouter, status

from src.api.dependencies import TransactionDep
from src.schemas.genres import (
    AddGenreSchema,
    GenreIdSchema,
    GenreSchema,
)
from src.services.genres import GenresService

router = APIRouter(
    prefix="/genres",
    tags=["Genres"]
)


@router.get(
    "/{genre_id}",
    status_code=status.HTTP_200_OK
)
async def get_genre(
        transaction: TransactionDep,
        genre_id: int
) -> GenreSchema:
    return await GenresService.get_genre(
        transaction,
        genre_id
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_all_genres(
        transaction: TransactionDep
) -> list[GenreSchema]:
    return await GenresService.get_all_genres(
        transaction
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def add_genre(
        transaction: TransactionDep,
        genre_data: AddGenreSchema
) -> GenreIdSchema:
    return await GenresService.add_genre(
        transaction,
        genre_data
    )


@router.put(
    "/{genre_id}",
    status_code=status.HTTP_200_OK
)
async def update_genre(
        transaction: TransactionDep,
        genre_id: int,
        new_name: str
) -> GenreIdSchema:
    return await GenresService.update_genre(
        transaction,
        genre_id,
        new_name
    )


@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_genre(
        transaction: TransactionDep,
        genre_id: int
) -> None:
    return await GenresService.delete_genre(
        transaction,
        genre_id
    )
