from typing import Any, Dict, List


class BaseController:
    def __init__(self, service, item_name: str):
        self.service = service
        self.NOT_FOUND_MSG = item_name + " not found."
        self.NOT_CREATED_MSG = item_name + " not created."

    def create(self, body) -> Dict:
        inserted_id: str | None = self.service.create(body)

        return {"id": inserted_id}

    def read_all(self) -> List[Any]:
        items: List[Any] = self.service.read_all()

        return items

    def read(self, id: str) -> Any:
        item: Any = self.service.read(id)

        return item

    def update(self, id: str, body) -> None:
        self.service.update(id, body)

    def delete(self, id: str) -> None:
        self.service.delete(id)
