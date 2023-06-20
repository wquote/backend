
from typing import List
from fastapi import APIRouter, Body, HTTPException, Path, Response, status

from app import business
from app.models.material import MaterialCreateModel, MaterialModel, MaterialUpdateModel


NOT_FOUND_MSG: str = 'Material not found.'

router = APIRouter(
    prefix='/materials'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(body: MaterialCreateModel, response: Response):
    inserted_id: str | None = business.material.create(body)

    if inserted_id is not None:
        response.headers["Location"] = inserted_id


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[MaterialModel])
async def read_all() -> List[MaterialModel]:
    materials: List[MaterialModel] = business.material.read_all()

    return materials


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=MaterialModel)
async def read(id: str):
    material: MaterialModel | None = business.material.read(id)
    if material is not None:
        return material

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: MaterialUpdateModel):
    if (business.material.update(id, body)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if (business.material.delete(id)):
        return None

    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
