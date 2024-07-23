from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    name: str
    price: float
    author_id: int
    genre_id: int
