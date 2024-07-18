from typing import List

from pydantic import EmailStr

from app.shared.base_model import AppBaseModel


class UserBase(AppBaseModel):
    username: str
    full_name: str | None = None
    email: EmailStr | None = None
    is_active: bool


class User(UserBase):
    id: str


class UserInDB(User):
    hashed_password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
