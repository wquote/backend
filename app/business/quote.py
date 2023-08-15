
from typing import Any, List

from app import services
from app.business.base import BaseBusiness
from app.models.quote import Quote, QuoteCreate


class QuoteBusiness(BaseBusiness):

    def create(self, item: QuoteCreate) -> str | None:
        pass

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items: List[Quote] = services.quote.read_by_customer(customer_id)

        return items

    def update(self, id: str, item: Any) -> None:
        pass


quote = QuoteBusiness(services.quote)
