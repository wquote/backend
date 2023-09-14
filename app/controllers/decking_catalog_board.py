
from typing import List
from fastapi import APIRouter, status

from app import services
from app.controllers.base import BaseController
from app.models.catalog import Catalog, CatalogCreate, CatalogUpdate

service = services.decking_catalog_board
TypeRead = Catalog
TypeCreate = CatalogCreate
TypeUpdate = CatalogUpdate
item_name = 'Decking Board catalog'

router = APIRouter(
    prefix='/decking/catalogs/board',
)

controller = BaseController(service, item_name)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TypeRead | None)
def create(body: TypeCreate):
    return controller.create(body)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[TypeRead])
def read_all() -> List[TypeRead] | None:
    items: List[TypeRead] | None = controller.read_all()
    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=TypeRead)
def read(id: str):
    item: TypeRead | None = controller.read(id)
    return item


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def update(id: str, body: TypeUpdate):
    return controller.update(id, body)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete(id: str):
    return controller.delete(id)
