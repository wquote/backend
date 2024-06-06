from typing import Dict, List

from fastapi import APIRouter, HTTPException, status

from app.decking_quote.decking_quote_models import (
    DeckingQuote,
    DeckingQuoteCreate,
    DeckingQuoteUpdate,
)
from app.decking_quote.decking_quote_service import decking_quote_service
from app.shared.base_controller import BaseController

service = decking_quote_service
TypeRead = DeckingQuote
TypeCreate = DeckingQuoteCreate
TypeUpdate = DeckingQuoteUpdate
item_name = "Decking Quote"

router = APIRouter(
    prefix="/quotes/decking",
)

controller = BaseController(service, item_name)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Dict | None)
def create(body: TypeCreate):
    return controller.create(body)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[TypeRead])
def read_all() -> List[TypeRead] | None:
    return controller.read_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TypeRead)
def read(id: str):
    return controller.read(id)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def update(id: str, body: TypeUpdate):
    return controller.update(id, body)


@router.put("/{id}/estimate", status_code=status.HTTP_200_OK, response_model=bool)
def estimate(id: str, body: TypeUpdate):
    if service.update_material_order(id, body):
        return True

    raise HTTPException(status_code=404, detail=item_name + " not found.")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete(id: str):
    return controller.delete(id)
