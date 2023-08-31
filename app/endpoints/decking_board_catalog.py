
from typing import List

from fastapi import APIRouter, HTTPException, status

from app import business
from app.models.catalog import Catalog, CatalogCreate, CatalogUpdate

NOT_FOUND_MSG: str = 'Catalog not found.'
business_controller = business.decking_board_catalog

router = APIRouter(
    prefix='/decking/board-catalog'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str | None)
async def create(body: CatalogCreate):
    inserted_id: str | None = business_controller.create(body)

    return {'id': inserted_id}


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Catalog])
async def read_all() -> List[Catalog]:
    items: List[Catalog] = business_controller.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Catalog)
async def read(id: str) -> Catalog:
    item: Catalog | None = business_controller.read(id)
    if item:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: CatalogUpdate):
    if (business_controller.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business_controller.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
