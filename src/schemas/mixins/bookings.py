from datetime import date
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
)


class DateMixin(BaseModel):
    date_from: date
    date_to: date


class RelationMixin(BaseModel):
    book_id: Annotated[int, Field(ge=1)]
    user_id: Annotated[int, Field(ge=1)]
