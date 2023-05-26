from fastapi import APIRouter, Depends

from auth.oauth2 import get_current_user
from users import schemas

router = APIRouter(
    tags=['user'],
    prefix='/users'
)

@router.get('/', response_model=schemas.User)
async def get_user(user = Depends(get_current_user)):
    return user