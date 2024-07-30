from pydantic import BaseModel

from src.schemas.mixins.genres import NameMixin


class GenreSchema(NameMixin):
    id: int


class AddGenreSchema(NameMixin):
    pass


class UpdateGenreSchema(NameMixin):
    pass


class GenreIdSchema(BaseModel):
    genre_id: int
