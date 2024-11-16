from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime
from typing import Annotated, Optional


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class UpdatePost(BasePost):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None

    # Sending the Post Out


class PostResponse(BasePost):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse


class Vote(BaseModel):
    post_id: int
    # to restrict the integer we received to be zero or one - used instead of conint which is deprecared
    dir: Annotated[int, Field(strict=True, ge=0, le=1)]
