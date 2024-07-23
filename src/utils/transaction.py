from abc import ABC, abstractmethod

from src.db.database import async_session_maker
from src.repositories.bookings import BookingsRepository
from src.repositories.books import BooksRepository
from src.repositories.genres import GenresRepository
from src.repositories.users import UsersRepository


class BaseManager(ABC):
    bookings_repo: BookingsRepository
    books_repo: BooksRepository
    genres_repo: GenresRepository
    users_repo: UsersRepository

    @abstractmethod
    def __init__(self):
        """Initializing the manager"""
        pass

    @abstractmethod
    async def __aenter__(self):
        """Enter the asynchronous context"""
        pass

    @abstractmethod
    async def __aexit__(self, *args):
        """Exit the asynchronous context"""
        pass

    @abstractmethod
    async def commit(self):
        """Commit the transaction"""
        pass

    @abstractmethod
    async def rollback(self):
        """Rollback the transaction"""
        pass


class TransactionManager(BaseManager):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.bookings_repo = BookingsRepository(self.session)
        self.books_repo = BooksRepository(self.session)
        self.genres_repo = GenresRepository(self.session)
        self.users_repo = UsersRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
