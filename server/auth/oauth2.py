from typing import Optional
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, WebSocketException, Query, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from auth import services

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/signin')


SECRET_KEY = '77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(username: str):
    refresh_token_data = {"sub": username, "type": "refresh"}
    refresh_token = create_access_token(
        refresh_token_data, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )
    return refresh_token


async def refresh_access_token(refresh_token: str):
    try:
        decoded_token = jwt.decode(
            refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded_token.get("sub")
        if username is None:
            raise JWTError
        user = user = await services.get_user(username)
        if user is None:
            raise JWTError
        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exc = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc

    user = await services.get_user(username)

    if user is None:
        raise credentials_exc
    return user


async def get_current_user_ws(token: str | None = Query(default=None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except JWTError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)

    user = await services.get_user(username)

    if user is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return user
