
from typing import Any, List, Type, TypeVar

from app.models.base import AppBaseModel


class BaseService():

    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, item) -> str | None:
        item_id: str | None = self.repository.create(item)
        return item_id if item_id else None

    def read_all(self) -> List:
        return self.repository.read_all()

    def read(self, id: str) -> Any:
        item = self.repository.read(id)
        return item if item else None

    def update(self, id: str, item) -> bool:
        return True if self.repository.update(id, item) else False

    def delete(self, id: str) -> bool:
        return True if self.repository.delete(id) else False
