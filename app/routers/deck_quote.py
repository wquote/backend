
from typing import List
from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.deck_quote import DeckQuoteCreateModel, DeckQuoteModel, DeckQuoteUpdateModel


NOT_FOUND_MSG: str = 'Deck quote not found.'

router = APIRouter(
    prefix='/quotes/decks'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: DeckQuoteCreateModel, response: Response):
    inserted_id: str | None = business.deck_quote.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckQuoteModel])
async def read_all() -> List[DeckQuoteModel]:
    items: List[DeckQuoteModel] = business.deck_quote.read_all()

    return items


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckQuoteModel)
async def read(id: str):
    item: DeckQuoteModel | None = business.deck_quote.read(id)
    if item is not None:
        return item

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: DeckQuoteUpdateModel):
    if (business.deck_quote.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete(id: str):
#     if (business.deck_quote.delete(id)):
#         return None

#     raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
