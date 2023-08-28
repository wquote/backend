
from typing import List
from fastapi import APIRouter, HTTPException, status

from app import business
from app.models.customer import Customer, CustomerCreate, CustomerUpdate


NOT_FOUND_MSG: str = 'Customer not found.'

router = APIRouter(
    prefix='/customers'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str | None)
async def create(body: CustomerCreate):
    inserted_id: str | None = business.customer.create(body)

    return inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Customer])
async def read_all() -> List[Customer]:
    items: List[Customer] = business.customer.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Customer)
async def read(id: str) -> Customer:
    item: Customer | None = business.customer.read(id)
    if item:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: CustomerUpdate):
    if (business.customer.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.customer.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
