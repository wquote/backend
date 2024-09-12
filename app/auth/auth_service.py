import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Literal

import jwt
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from app.shared.base_model import AppBaseModel
from app.shared.base_repository import raise_error
from app.user.user_model import User, UserInDB
from app.user.user_service import user_service

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


class Token(AppBaseModel):
    access_token: str
    token_type: str


SECRET_KEY: str = os.getenv("AUTH_SECRET_KEY") or ""
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

router = APIRouter()

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def get_user(username: str) -> UserInDB:
    user: UserInDB | None = user_service.read_by_username(username)
    if not user:
        raise credentials_exception

    return user


def authenticate_user(username: str, password: str) -> UserInDB | Literal[False]:
    user: UserInDB = get_user(username)
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta | None) -> str:
    to_encode: dict = data.copy()

    if not expires_delta:
        expires_delta = timedelta(minutes=15)
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserInDB:
    try:
        token_payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = token_payload.get("sub")
        if username is None:
            raise credentials_exception

        user: UserInDB = get_user(username)

    except jwt.ExpiredSignatureError:
        raise credentials_exception

    except Exception as e:
        raise_error(e)

    return user


async def get_current_active_user(current_user: Annotated[UserInDB, Depends(get_current_user)]) -> UserInDB:
    if not current_user.is_active:
        raise credentials_exception

    return current_user


async def is_authenticated(current_user: Annotated[UserInDB, Depends(get_current_user)]) -> bool:
    return True if current_user.is_active else False


@router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]) -> Token:
    try:
        user: UserInDB | Literal[False] = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise credentials_exception

        access_token: str = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    except Exception as e:
        raise_error(e)

    return Token(access_token=access_token, token_type="bearer")


@router.get("/auth/token/validate")
async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        token_payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Token is valid."}
    except jwt.ExpiredSignatureError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")


@router.get("/users/me", response_model=User)
async def read_current_user(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/me/items")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
