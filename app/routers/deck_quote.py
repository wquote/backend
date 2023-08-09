
from typing import List
from fastapi import APIRouter, HTTPException, status

from app import business
from app.models.deck_quote import DeckQuote, DeckQuoteCreate, DeckQuoteUpdate


NOT_FOUND_MSG: str = 'Deck quote not found.'

router = APIRouter(
    prefix='/quotes/decks'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str | None)
async def create(body: DeckQuoteCreate):
    inserted_id: str | None = business.deck_quote.create(body)

    return inserted_id


# @router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckQuote])
# async def read_all() -> List[DeckQuote]:
#     items: List[DeckQuote] = business.deck_quote.read_all()

#     return items


# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckQuote)
# async def read(id: str) -> DeckQuote:
#     item: DeckQuote | None = business.deck_quote.read(id)
#     if item is not None:
#         return item

#     raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


# @router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# async def update(id: str, body: DeckQuoteUpdate):
#     if (business.deck_quote.update(id, body)):
#         return None

#     raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete(id: str):
#     if (business.deck_quote.delete(id)):
#         return None

#     raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
