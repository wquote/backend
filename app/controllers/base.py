from typing import Any, List, Type, TypeVar

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from app.models.base import AppBaseModel

C = TypeVar('C')  # create
R = TypeVar('R')  # read
U = TypeVar('U')  # update


class BaseEndpoint():
    def __init__(self, business_controller, item_name: str, read_model: R, create_model: C, update_model: U):
        self.business_controller = business_controller
        self.create_model = create_model
        self.read_model = read_model
        self.update_model = update_model
        self.NOT_FOUND_MSG = item_name + ' not found.'
        self.NOT_CREATED_MSG = item_name + ' not created.'

    def create(self, body: C) -> JSONResponse:
        inserted_id: str | None = self.business_controller.create(body)

        if inserted_id is None:
            raise HTTPException(status_code=400, detail=self.NOT_CREATED_MSG)

        return JSONResponse(status_code=status.HTTP_201_CREATED, content={'id': inserted_id})

    def read_all(self) -> List[R] | None:
        items: List[R] | None = self.business_controller.read_all()
        if items is None:
            raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

        return items

    def read(self, id: str) -> R | None:
        item: R | None = self.business_controller.read(id)
        if item:
            return item

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def update(self, id: str, body: U) -> None:
        if (self.business_controller.update(id, body)):
            return None

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def delete(self, id: str) -> None:
        if (self.business_controller.delete(id)):
            return None

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)
