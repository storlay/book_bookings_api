from pydantic import BaseModel


class GenreSchema(BaseModel):
    id: int
    name: str


class AddGenreSchema(BaseModel):
    name: str


class GenreIdSchema(BaseModel):
    genre_id: int
