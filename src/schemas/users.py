from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    avatar_path: Optional[str]
