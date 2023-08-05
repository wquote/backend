from typing import List

from app import services
from app.models.customer import Customer, CustomerCreate, CustomerUpdate


class CustomerBusiness():
    def create(self, item: CustomerCreate) -> str | None:
        item_id: str | None = services.customer.create(item)

        return item_id if item_id is not None else None

    def read_all(self) -> List[Customer]:
        items: List[Customer] = services.customer.read_all()

        return items

    def read(self, id: str) -> Customer | None:
        item: Customer | None = services.customer.read(id)

        return item if item is not None else None

    def update(self, id: str, item: CustomerUpdate) -> bool | None:
        if (services.customer.update(id, item)):
            return True

        return None

    def delete(self, id: str):
        if (services.customer.delete(id)):
            return True

        return None


customer = CustomerBusiness()
