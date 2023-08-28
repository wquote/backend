
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.decking_board_catalog import (DeckingBoardCatalog,
                                              DeckingBoardCatalogCreate,
                                              DeckingBoardCatalogUpdate)

NOT_FOUND_MSG: str = 'Deck board type not found.'

router = APIRouter(
    prefix='/decking/board-catalogs',
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: DeckingBoardCatalogCreate, response: Response):
    inserted_id: str | None = business.decking_board_catalog.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[DeckingBoardCatalog])
async def read_all() -> List[DeckingBoardCatalog]:
    deckboard_types: List[DeckingBoardCatalog] = business.decking_board_catalog.read_all(
    )

    return deckboard_types


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DeckingBoardCatalog)
async def read(id: str):
    deckboard_type: DeckingBoardCatalog | None = business.decking_board_catalog.read(id)
    if deckboard_type is not None:
        return deckboard_type

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: DeckingBoardCatalogUpdate):
    if (business.decking_board_catalog.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.decking_board_catalog.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
