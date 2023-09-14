
from typing import List

from app import repositories
from app.services.base import BaseService
from app.models.quote import Quote


class QuoteService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items: List[Quote] = repositories.quote.read_by_customer(customer_id)

        return items


quote = QuoteService(repositories.quote)
