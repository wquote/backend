
from typing import List
from fastapi import APIRouter

from app import business
from app.endpoints.base import BaseEndpoint
from app.models.customer import Customer, CustomerCreate, CustomerUpdate

business_controller = business.customer
TypeRead = Customer
TypeCreate = CustomerCreate
TypeUpdate = CustomerUpdate
item_name = 'Customer'

router = APIRouter(
    prefix='/customers'
)

endpoint = BaseEndpoint(business_controller, item_name, Customer, CustomerCreate, CustomerUpdate)


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
