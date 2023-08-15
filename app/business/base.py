
from typing import List, Type, TypeVar

from app.models.base import AppBaseModel

C = TypeVar('C', bound=AppBaseModel)  # create
R = TypeVar('R', bound=AppBaseModel)  # read


class BaseBusiness():

    def __init__(self, service_name, read_model: Type[R] | None = None) -> None:
        self.service_name = service_name
        self.read_model = read_model

    def create(self, item) -> str | None:
        item_id: str | None = self.service_name.create(item)
        return item_id if item_id is not None else None

    def read_all(self) -> List[R]:
        items: List = self.service_name.read_all()
        return items

    def read(self, id: str) -> R | None:
        item: R | None = self.service_name.read(id)
        return item if item is not None else None

    def update(self, id: str, item: R) -> bool | None:
        if self.service_name.update(id, item):
            return True
        return None

    def delete(self, id: str):
        if self.service_name.delete(id):
            return True
        return None
