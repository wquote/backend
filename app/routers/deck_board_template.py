
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.deck_board_template import (DeckBoardTemplateCreateModel, DeckBoardTemplateModel,
                                            DeckBoardTemplateUpdateModel)


NOT_FOUND_MSG: str = 'Deck board type not found.'

router = APIRouter(
    prefix='/decks/board-templates'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: DeckBoardTemplateCreateModel, response: Response):
    inserted_id: str | None = business.deck_board_template.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckBoardTemplateModel])
async def read_all() -> List[DeckBoardTemplateModel]:
    deckboard_types: List[DeckBoardTemplateModel] = business.deck_board_template.read_all()

    return deckboard_types


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckBoardTemplateModel)
async def read(id: str):
    deckboard_type: DeckBoardTemplateModel | None = business.deck_board_template.read(id)
    if deckboard_type is not None:
        return deckboard_type

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: DeckBoardTemplateUpdateModel):
    if (business.deck_board_template.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.deck_board_template.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
