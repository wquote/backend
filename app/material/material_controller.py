from typing import Dict, List

from fastapi import APIRouter, Depends, status

from app.auth.auth_service import is_authenticated
from app.material.material_models import Material, MaterialCreate, MaterialUpdate
from app.material.material_service import material_service
from app.shared.base_controller import BaseController

service = material_service
TypeRead = Material
TypeCreate = MaterialCreate
TypeUpdate = MaterialUpdate
item_name = "Material"

router = APIRouter(
    prefix="/materials",
    dependencies=[Depends(is_authenticated)],
)

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
