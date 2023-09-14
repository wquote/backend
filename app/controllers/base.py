
from typing import Any, Dict, List

from fastapi import HTTPException


class BaseController():
    def __init__(self, service, item_name: str):
        self.service = service
        self.NOT_FOUND_MSG = item_name + ' not found.'
        self.NOT_CREATED_MSG = item_name + ' not created.'

    def create(self, body) -> Dict:
        inserted_id: str | None = self.service.create(body)

        if inserted_id:
            return {'id': inserted_id}

        raise HTTPException(status_code=400, detail=self.NOT_CREATED_MSG)

    def read_all(self) -> List | None:
        items: List | None = self.service.read_all()
        if items:
            return items

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def read(self, id: str) -> Any | None:
        if item := self.service.read(id):
            return item

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def update(self, id: str, body) -> bool:
        if (self.service.update(id, body)):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def delete(self, id: str) -> bool:
        if (self.service.delete(id)):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)
