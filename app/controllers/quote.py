
from typing import List

from fastapi import APIRouter, HTTPException, status

from app import services
from app.models.quote import Quote

NOT_FOUND_MSG: str = 'Quote not found.'
service = services.quote

router = APIRouter(
    prefix='/quotes'
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Quote])
async def read_all(type: str | None = None, customerId: str | None = None) -> List[Quote]:
    items: List[Quote] = []

    if customerId:
        items = service.read_by_customer(customerId)
    else:
        items = service.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Quote)
async def read(id: str):
    item: Quote | None = service.read(id)
    if item:
        return item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (services.quote.delete(id)):
        return None

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MSG)
