from typing import Dict, List, Type, TypeVar

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

R = TypeVar('R')  # read
C = TypeVar('C')  # create
U = TypeVar('U')  # update


class BaseController():
    def __init__(self, service, item_name: str, read_model: Type[R], create_model: Type[C], update_model: Type[U]):
        self.service = service
        self.read_model = read_model
        self.create_model = create_model
        self.update_model = update_model
        self.NOT_FOUND_MSG = item_name + ' not found.'
        self.NOT_CREATED_MSG = item_name + ' not created.'

    def create(self, body: C) -> Dict:
        inserted_id: str | None = self.service.create(body)

        if inserted_id is None:
            raise HTTPException(status_code=400, detail=self.NOT_CREATED_MSG)

        return {'id': inserted_id}

    def read_all(self) -> List[R] | None:
        items: List[R] | None = self.service.read_all()
        if items is None:
            raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

        return items

    def read(self, id: str) -> R | None:
        if item := self.service.read(id):
            return item

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def update(self, id: str, body: U) -> bool:
        if (self.service.update(id, body)):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def delete(self, id: str) -> bool:
        if (self.service.delete(id)):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)
