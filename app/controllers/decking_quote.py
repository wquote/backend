
from typing import List
from fastapi import APIRouter

from app import services
from app.controllers.base import BaseEndpoint
from app.models.decking_quote import DeckingQuote, DeckingQuoteCreate, DeckingQuoteUpdate

business_controller = services.decking_quote
TypeRead = DeckingQuote
TypeCreate = DeckingQuoteCreate
TypeUpdate = DeckingQuoteUpdate
item_name = 'Decking Quote'

router = APIRouter(
    prefix='/quotes/decking',
)

endpoint = BaseEndpoint(business_controller, item_name, DeckingQuote, DeckingQuoteCreate, DeckingQuoteUpdate)


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
