from src.models.genres import Genres
from src.utils.repository import BaseRepository


class GenresRepository(BaseRepository):
    model = Genres
