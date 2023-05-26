from datetime import timedelta

from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from . import schemas
from . import services
from .hash import Hash
from auth import oauth2

router = APIRouter(
    tags=['auth'],
    prefix='/auth'
)


@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(request: schemas.UserCredentials):
    await services.create_user(request.username, request.password)

@router.post("/refresh-token")
async def refresh_access_token(token_data: schemas.RefreshToken):
    new_access_token = await oauth2.refresh_access_token(token_data.refresh_token)
    return new_access_token


@router.post('/signin', status_code=status.HTTP_201_CREATED)
async def sign_in(request: OAuth2PasswordRequestForm = Depends()):
    user = await services.get_user(request.username)
    if not user:
        raise HTTPException(status_code=404, detail='invalid creadentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail='Incorrect password')

    access_token = oauth2.create_access_token(
        {'sub': user.username}, timedelta(minutes=oauth2.ACCESS_TOKEN_EXPIRE_MINUTES))
    refresh_token = oauth2.create_refresh_token(user.username)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "Bearer"}
