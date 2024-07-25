from sqlalchemy import (
    delete,
    insert,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        statement = (
            insert(self.model)
            .values(**data)
            .returning(self.model.id)
        )
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def delete_one(self, obj_id: int) -> None:
        statement = (
            delete(self.model)
            .filter_by(id=obj_id)
            .returning(self.model.id)
        )
        await self.session.execute(statement)

    async def edit_one(self, obj_id: int, data: dict) -> int:
        statement = (
            update(self.model)
            .values(**data)
            .filter_by(id=obj_id)
            .returning(self.model.id)
        )
        result = await self.session.execute(statement)
        return result.scalar_one()

    async def find_one(self, **filter_by):
        statement = (
            select(self.model)
            .filter_by(**filter_by)
        )
        result = await self.session.execute(statement)
        return result.scalar_one().to_read_model()

    async def find_all(self):
        statement = select(self.model)
        result = await self.session.execute(statement)
        result = [row[0].to_read_model() for row in result.all()]
        return result
