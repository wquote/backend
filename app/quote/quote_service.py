from typing import List

from app.quote.quote_model import Quote
from app.quote.quote_repository import quote_repository
from app.shared.base_service import BaseService


class QuoteService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items: List[Quote] = quote_repository.read_by_customer(customer_id)

        return items


quote_service: QuoteService = QuoteService(quote_repository)
