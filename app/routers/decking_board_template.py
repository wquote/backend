
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.decking_board_template import (DeckingBoardTemplate,
                                               DeckingBoardTemplateCreate,
                                               DeckingBoardTemplateUpdate)

NOT_FOUND_MSG: str = 'Deck board type not found.'

router = APIRouter(
    prefix='/decks/board-templates'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: DeckingBoardTemplateCreate, response: Response):
    inserted_id: str | None = business.decking_board_template.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckingBoardTemplate])
async def read_all() -> List[DeckingBoardTemplate]:
    deckboard_types: List[DeckingBoardTemplate] = business.decking_board_template.read_all(
    )

    return deckboard_types


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckingBoardTemplate)
async def read(id: str):
    deckboard_type: DeckingBoardTemplate | None = business.decking_board_template.read(id)
    if deckboard_type is not None:
        return deckboard_type

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: DeckingBoardTemplateUpdate):
    if (business.decking_board_template.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.decking_board_template.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
