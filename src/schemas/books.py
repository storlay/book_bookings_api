from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    name: str
    price: float
    author_id: int
    genres: list[str]


class BookIdSchema(BaseModel):
    book_id: int


class AddBookSchema(BaseModel):
    name: str
    price: float
    author_id: int


class UpdateBookSchema(BaseModel):
    name: Optional[str]
    price: Optional[float]
    author_id: Optional[int]
