from typing import List, TypeVar, Generic, Optional
from services import customer, material, quote
import services

T = TypeVar('T')  # Placeholder for the specific model type


class BaseBusiness(Generic[T]):

    model_name = ''

    def create(self, item: T) -> str | None:
        item_id: str | None = services[self.model_name].create(item)
        return item_id if item_id is not None else None

    def read_all(self) -> List[T]:
        items: List[T] = services[self.model_name].read_all()
        return items

    def read(self, id: str) -> T | None:
        item: T | None = services[self.model_name].read(id)
        return item if item is not None else None

    def update(self, id: str, item: T) -> bool | None:
        if services[self.model_name].update(id, item):
            return True
        return None

    def delete(self, id: str):
        if services[self.model_name].delete(id):
            return True
        return None
