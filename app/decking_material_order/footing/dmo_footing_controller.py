from typing import Dict, List

from fastapi import APIRouter, status

from app.shared.base_controller import BaseController
from app.shared.material_order_model import (
    MaterialOrderCreate,
    MaterialOrderDTO,
    MaterialOrderUpdate,
)

from .dmo_footing_service import dmo_footing_service

service = dmo_footing_service
TypeRead = MaterialOrderDTO
TypeCreate = MaterialOrderCreate
TypeUpdate = MaterialOrderUpdate
item_name = "Decking Material Order Footings"

router = APIRouter(
    prefix="/decking/material-order/footings",
)

controller = BaseController(service, item_name)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Dict | None)
def create(body: TypeCreate):
    return controller.create(body)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[TypeRead])
def read_all() -> List[TypeRead] | None:
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
