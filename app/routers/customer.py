
from typing import List
from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.customer import CustomerModel, CustomerCreateModel, CustomerUpdateModel


NOT_FOUND_MSG: str = 'Customer not found.'

router = APIRouter(
    prefix='/customers'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: CustomerCreateModel, response: Response):
    inserted_id: str | None = business.customer.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CustomerModel])
async def read_all() -> List[CustomerModel]:
    items: List[CustomerModel] = business.customer.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=CustomerModel)
async def read(id: str):
    item: CustomerModel | None = business.customer.read(id)
    if item is not None:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: CustomerUpdateModel):
    if (business.customer.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.customer.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
