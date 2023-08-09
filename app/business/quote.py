
from typing import List

from app import services
from app.models.quote import Quote


class QuoteBusiness():

    def read(self, id: str) -> Quote | None:
        if (item := services.quote.read(id)) is not None:
            return item

        return None

    def read_all(self) -> List[Quote]:
        items: List[Quote] = services.quote.read_all()

        return items

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items: List[Quote] = services.quote.read_by_customer(customer_id)

        return items

    def delete(self, id: str):
        if (services.quote.delete(id)):
            return True

        return None


quote = QuoteBusiness()
