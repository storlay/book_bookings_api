from src.models.users import Users
from src.utils.repository import BaseRepository


class UsersRepository(BaseRepository):
    model = Users
