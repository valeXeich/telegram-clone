from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, validator

from .utils import format_created_at


class User(BaseModel):
    id: int
    username: str
    avatar: str

    class Config:
        orm_mode = True


class Message(BaseModel):
    id: int
    file: Optional[str] = None
    file_name: Optional[str] = None
    content: str
    is_file: bool
    readed: bool
    file_type: Optional[str] = None
    size: Optional[int]
    created_at: str
    user: Optional[User]

    @validator('created_at', pre=True, always=True)
    def format_created_at(cls, value):
        return format_created_at(value)


class RoomList(BaseModel):
    id: int
    user: User
    message: Optional[Message]

    class Config:
        orm_mode = True


class Room(BaseModel):
    id: int
    user: User
    messages: Optional[List[Message]]
