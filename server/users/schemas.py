from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    avatar: str
    bio: Optional[str]