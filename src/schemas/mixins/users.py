from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
)


class InitialsMixin(BaseModel):
    first_name: Annotated[str, Field(min_length=2, max_length=100)]
    last_name: Annotated[str, Field(min_length=2, max_length=100)]
