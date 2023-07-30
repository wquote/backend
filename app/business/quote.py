
from typing import List

from app import services
from app.models.quote import QuoteModel


class QuoteBusiness():

    def read(self, id: str) -> QuoteModel | None:
        if (item := services.quote.read(id)) is not None:
            return item

        return None

    def read_all(self) -> List[QuoteModel]:
        items: List[QuoteModel] = services.quote.read_all()

        return items

    def read_by_customer(self, id_customer: str) -> List[QuoteModel]:
        items: List[QuoteModel] = services.quote.read_by_customer(id_customer)

        return items

    def delete(self, id: str):
        if (services.quote.delete(id)):
            return True

        return None


quote = QuoteBusiness()
