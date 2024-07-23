from pydantic import BaseModel

from typing import Optional


class BookSchema(BaseModel):
    id: int
    name: str
    price: float
    author_id: int
    genre_id: int


class BookIdSchema(BaseModel):
    book_id: int


class AddBookSchema(BaseModel):
    name: str
    price: float
    author_id: int
    genre_id: int


class UpdateBookSchema(BaseModel):
    name: Optional[str]
    price: Optional[float]
    author_id: Optional[int]
    genre_id: Optional[int]
