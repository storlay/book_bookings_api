from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
)

from src.schemas.mixins.books import (
    NameMixin,
    PriceMixin,
    RelationAuthorMixin,
)


class BookSchema(
    NameMixin,
    PriceMixin,
    RelationAuthorMixin,
):
    id: int
    genres: list[str]


class BookFiltersSchema(BaseModel):
    author_name: Annotated[str | None, Field(None)]
    author_surname: Annotated[str | None, Field(None)]
    min_price: Annotated[float | None, Field(None, ge=0)]
    max_price: Annotated[float | None, Field(None, ge=0)]


class BookIdSchema(BaseModel):
    book_id: int


class AddBookSchema(
    NameMixin,
    PriceMixin,
    RelationAuthorMixin,
):
    pass


class UpdateBookSchema(
    NameMixin,
    PriceMixin,
    RelationAuthorMixin,
):
    pass
