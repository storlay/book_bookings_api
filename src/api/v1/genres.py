from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    status,
)

from src.api.dependencies import TransactionDep
from src.api.pagination import (
    BasePaginationResponse,
    PaginationParams,
    Paginator,
)
from src.schemas.genres import (
    AddGenreSchema,
    GenreIdSchema,
    GenreSchema,
    UpdateGenreSchema,
)
from src.services.genres import GenresService

router = APIRouter(
    prefix="/genres",
    tags=["Genres"],
)


@router.get(
    "/all",
    status_code=status.HTTP_200_OK,
)
async def get_all_genres(
    transaction: TransactionDep,
    pagination: PaginationParams = Depends(),
) -> BasePaginationResponse[GenreSchema]:
    """
    Getting all genres.
    :param transaction: Database transaction.
    :param pagination: Pagination params.
    :return: List of Pydantic models representing the genre.
    """
    list_genres = await GenresService.get_all_genres(
        transaction,
    )
    paginator = Paginator(
        pages=list_genres,
        params=pagination,
    )
    return paginator.get_response()


@router.get(
    "/{genre_id}",
    status_code=status.HTTP_200_OK,
)
async def get_genre(
    transaction: TransactionDep,
    genre_id: Annotated[int, Path(ge=1)],
) -> GenreSchema:
    """
    Getting a genre by ID.
    :param transaction: Database transaction.
    :param genre_id: Genre ID.
    :return: Pydantic model representing the genre.
    """
    return await GenresService.get_genre(
        transaction,
        genre_id,
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def add_genre(
    transaction: TransactionDep,
    genre_data: AddGenreSchema = Depends(),
) -> GenreIdSchema:
    """
    Adding a new genre.
    :param transaction: Database transaction.
    :param genre_data: Pydantic model representing genre data.
    :return: Pydantic model representing the created genre ID.
    """
    return await GenresService.add_genre(
        transaction,
        genre_data,
    )


@router.put(
    "/{genre_id}",
    status_code=status.HTTP_200_OK,
)
async def update_genre(
    transaction: TransactionDep,
    genre_id: Annotated[int, Path(ge=1)],
    genre_data: UpdateGenreSchema = Depends(),
) -> GenreIdSchema:
    """
    Updating a genre by ID.
    :param transaction: Database transaction.
    :param genre_id: Genre ID.
    :param genre_data: Pydantic model representing genre data.
    :return: Pydantic model representing the updated genre ID.
    """
    return await GenresService.update_genre(
        transaction,
        genre_id,
        genre_data,
    )


@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_genre(
    transaction: TransactionDep,
    genre_id: Annotated[int, Path(ge=1)],
) -> None:
    """
    Deleting a genre by ID.
    :param transaction: Database transaction.
    :param genre_id: Genre ID.
    :return: None.
    """
    return await GenresService.delete_genre(
        transaction,
        genre_id,
    )
