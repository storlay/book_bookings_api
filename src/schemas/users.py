from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    avatar_path: Optional[str]


class UserIdSchema(BaseModel):
    user_id: int


class UserInitialsSchema(BaseModel):
    first_name: str
    last_name: str
