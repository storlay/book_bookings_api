from typing import Sequence

from sqlalchemy import select

from src.exceptions.genres import IncorrectNamesOfGenreException
from src.models.genres import Genres
from src.utils.repository import BaseRepository


class GenresRepository(BaseRepository):
    model = Genres

    async def find_by_names(
            self,
            names: list[str],
    ) -> Sequence[Genres]:
        """
        Search for genres by name.
        :param names: List of names.
        :return: List of genre models.
        """
        query = (
            select(self.model)
            .filter(self.model.name.in_(names))
        )
        result = await self.session.execute(query)
        genres = result.unique().scalars().all()
        if len(genres) == len(names):
            return genres
        raise IncorrectNamesOfGenreException
