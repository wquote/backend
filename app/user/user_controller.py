from typing import Dict, List

from fastapi import APIRouter, status

from app.shared.base_controller import BaseController

from .user_model import User, UserCreate, UserUpdate
from .user_service import user_service

service = user_service
TypeRead = User
TypeCreate = UserCreate
TypeUpdate = UserUpdate
item_name = "User"

router = APIRouter(prefix="/users")

controller = BaseController(service, item_name)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Dict)
def create(body: TypeCreate):
    return controller.create(body)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[TypeRead])
def read_all() -> List[TypeRead]:
    return controller.read_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TypeRead)
def read(id: str):
    return controller.read(id)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def update(id: str, body: TypeUpdate):
    return controller.update(id, body)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete(id: str):
    return controller.delete(id)
