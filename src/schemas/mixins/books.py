from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
)


class PriceMixin(BaseModel):
    price: Annotated[float, Field(ge=1)]


class RelationAuthorMixin(BaseModel):
    author_id: Annotated[int, Field(ge=1)]


class NameMixin(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100)]
