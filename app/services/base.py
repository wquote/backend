
from typing import List, Type, TypeVar

from app.models.base import AppBaseModel

C = TypeVar('C', bound=AppBaseModel)  # create
R = TypeVar('R', bound=AppBaseModel)  # read


class BaseService():

    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, item) -> str | None:
        item_id: str | None = self.repository.create(item)
        return item_id if item_id else None

    def read_all(self) -> List[R]:
        items: List[R] = self.repository.read_all()
        return items

    def read(self, id: str) -> R | None:
        item: R | None = self.repository.read(id)
        return item if item else None

    def update(self, id: str, item) -> bool:
        if self.repository.update(id, item):
            return True
        return False

    def delete(self, id: str) -> bool:
        if self.repository.delete(id):
            return True
        return False
