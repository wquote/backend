
from typing import List
from fastapi import APIRouter

from app import services
from app.controllers.base import BaseEndpoint
from app.models.material import Material, MaterialCreate, MaterialUpdate

business_controller = services.material
TypeRead = Material
TypeCreate = MaterialCreate
TypeUpdate = MaterialUpdate
item_name = 'Material'

router = APIRouter(
    prefix='/materials'
)

endpoint = BaseEndpoint(business_controller, item_name, Material, MaterialCreate, MaterialUpdate)


@router.post('/', response_model=TypeRead | None)
def create(body: TypeCreate):
    return endpoint.create(body)


@router.get('/', response_model=List[TypeRead])
def read_all() -> List[TypeRead] | None:
    items: List[TypeRead] | None = endpoint.read_all()
    return items


@router.get('/{id}', response_model=TypeRead)
def read(id: str):
    item: TypeRead | None = endpoint.read(id)
    return item


@router.put('/{id}')
def update(id: str, body: TypeUpdate):
    return endpoint.update(id, body)


@router.delete('/{id}')
def delete(id: str):
    return endpoint.delete(id)
