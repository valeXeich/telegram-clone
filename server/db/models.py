import datetime
from typing import Optional, List

import ormar

from .database import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'
    
    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=50, unique=True)
    avatar: str = ormar.Text(default='http://127.0.0.1:8000/media/default/avatar')
    bio: str = ormar.String(max_length=70, nullable=True)
    password: str = ormar.String(max_length=250)


class Message(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'messages'
    
    id: int = ormar.Integer(primary_key=True)
    file: str = ormar.Text(nullable=True)
    file_name: str = ormar.String(max_length=255, nullable=True)
    content: str = ormar.Text(nullable=True)
    is_file: bool = ormar.Boolean(default=False)
    readed: bool = ormar.Boolean(default=False)
    size: bytes = ormar.Integer(nullable=True)
    file_type: str = ormar.String(max_length=30, nullable=True)
    user: Optional[User] = ormar.ForeignKey(User)
    created_at: datetime.datetime = ormar.DateTime(
        default=datetime.datetime.utcnow
    )
    updated_at: datetime.datetime = ormar.DateTime(
        default=datetime.datetime.utcnow,
        server_default="now()"
    )


class Room(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'rooms'
    
    id: int = ormar.Integer(primary_key=True)
    messages: Optional[List[Message]] = ormar.ManyToMany(Message)
    users: Optional[List[User]] = ormar.ManyToMany(User)

