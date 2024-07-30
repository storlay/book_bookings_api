from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
)


class NameMixin(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=30)]
