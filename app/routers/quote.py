
from typing import List
from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.quote import QuoteModel


NOT_FOUND_MSG: str = 'Quote not found.'

router = APIRouter(
    prefix='/quotes'
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[QuoteModel])
async def read_all(idCustomer: str | None = None) -> List[QuoteModel]:
    items: List[QuoteModel] = []

    if idCustomer:
        items = business.quote.read_by_customer(idCustomer)
    else:
        items = business.quote.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=QuoteModel)
async def read(id: str):
    item: QuoteModel | None = business.quote.read(id)
    if item is not None:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.quote.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
