from typing import Annotated

from pydantic import BaseModel, Field

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
