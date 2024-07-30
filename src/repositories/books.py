from sqlalchemy import (
    and_,
    insert,
    select,
    update,
)
from sqlalchemy.orm import selectinload

from src.models.books import Books
from src.models.genres import Genres
from src.schemas.books import BookSchema
from src.utils.repository import BaseRepository


class BooksRepository(BaseRepository):
    model = Books

    async def add_one(self, book_data: dict) -> Books:
        """
        Adding a book to the database.
        :param book_data: Book data.
        :return: The model of the created book.
        """
        statement = (
            insert(self.model)
            .values(**book_data)
            .returning(self.model)
        )
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def edit_one(self, obj_id: int, data: dict) -> Books:
        """
        Updating a book in the database.
        :param obj_id: Book ID.
        :param data: Editable data.
        :return: The model of the updated book.
        """
        statement = (
            update(self.model)
            .values(**data)
            .filter_by(id=obj_id)
            .returning(self.model)
        )
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def find_with_filters(
        self,
        author_name: str = None,
        author_surname: str = None,
        genres: list[str] = None,
        min_price: float = None,
        max_price: float = None,
    ) -> list[BookSchema]:
        """
        Search for books in the database by filters.
        :param author_name: Author's name.
        :param author_surname: Author's surname
        :param genres: List of genres.
        :param min_price: Minimal price.
        :param max_price: Maximum price.
        :return: List of Pydantic models representing the book.
        """
        statement = select(self.model)
        filters = []

        if author_name:
            filters.append(self.model.author.has(first_name=author_name))
        if author_surname:
            filters.append(self.model.author.has(last_name=author_surname))
        if genres:
            statement = statement.options(selectinload(self.model.genres))
            filters.append(self.model.genres.any(Genres.name.in_(genres)))
        if min_price:
            filters.append(self.model.price >= min_price)
        if max_price:
            filters.append(self.model.price <= max_price)

        if filters:
            statement = statement.filter(and_(*filters))

        result = await self.session.execute(statement)
        result = [row[0].to_read_model() for row in result.all()]
        return result
