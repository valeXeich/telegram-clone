from fastapi import HTTPException, status

from db.models import User
from .hash import Hash


async def create_user(username: str, password: str):
    hashed_password = Hash.bcrypt(password)
    user, created = await User.objects.get_or_create(username=username, _defaults={'password': hashed_password})
    if not created:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "This username is busy")
    return user


async def get_user(username: str):
    user = await User.objects.get_or_none(username=username)
    return user