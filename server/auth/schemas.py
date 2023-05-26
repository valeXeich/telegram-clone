from pydantic import BaseModel, constr, validator

class UserCredentials(BaseModel):
    username: str
    password: constr(min_length=8)

    @validator('password')
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class RefreshToken(BaseModel):
    refresh_token: str