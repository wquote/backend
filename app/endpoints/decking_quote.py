
from typing import List
from fastapi import APIRouter, HTTPException, status

from app import business
from app.models.decking_quote import DeckingQuote, DeckingQuoteCreate, DeckingQuoteUpdate


NOT_FOUND_MSG: str = 'Decking quote not found.'

router = APIRouter(
    prefix='/quotes/decking'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str | None)
async def create(body: DeckingQuoteCreate):
    inserted_id: str | None = business.decking_quote.create(body)

    return inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckingQuote])
async def read_all() -> List[DeckingQuote]:
    items: List[DeckingQuote] = business.decking_quote.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckingQuote)
async def read(id: str) -> DeckingQuote:
    item: DeckingQuote | None = business.decking_quote.read(id)
    if item is not None:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: DeckingQuoteUpdate):
    if (business.decking_quote.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.decking_quote.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
