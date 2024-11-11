from pydantic import BaseModel, EmailStr
from datetime import datetime


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class UpdatePost(BasePost):
    pass


class PostResponse(BasePost):
    id: int
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    email: EmailStr
