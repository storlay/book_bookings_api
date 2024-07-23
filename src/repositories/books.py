from src.models.books import Books
from src.utils.repository import BaseRepository


class BooksRepository(BaseRepository):
    model = Books
