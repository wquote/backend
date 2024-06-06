from typing import List

from fastapi import APIRouter, HTTPException, status

from app.quote.quote_models import Quote, QuoteCreate, QuoteUpdate
from app.quote.quote_service import quote_service
from app.shared.base_controller import BaseController

NOT_FOUND_MSG: str = "Quote not found."
service = quote_service
TypeRead = Quote
TypeCreate = QuoteCreate
TypeUpdate = QuoteUpdate
item_name = "Quote"

router = APIRouter(prefix="/quotes")

contoller = BaseController(service, item_name)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Quote])
def read_all(customerId: str | None = None) -> List[Quote]:
    items: List[Quote] = []

    if customerId:
        items = service.read_by_customer(customerId)
    else:
        items = service.read_all()

    return items


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Quote)
def read(id: str):
    return contoller.read(id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    return contoller.delete(id)
