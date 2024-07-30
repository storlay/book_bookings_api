from pydantic import BaseModel

from src.schemas.mixins.users import InitialsMixin


class UserSchema(InitialsMixin):
    id: int
    avatar_path: str | None


class UserIdSchema(BaseModel):
    user_id: int


class UserInitialsSchema(InitialsMixin):
    pass
