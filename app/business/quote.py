
from typing import List

from app import services
from app.models.quote import QuoteModel


class QuoteBusiness():

    def read_all(self) -> List[QuoteModel]:
        deck_quotes: List[QuoteModel] = services.quote.read_all()

        return deck_quotes

    def read(self, id: str) -> QuoteModel | None:
        if (deck_quote := services.quote.read(id)) is not None:
            return deck_quote

        return None

    def delete(self, id: str):
        if (services.quote.delete(id)):
            return True

        return None


quote = QuoteBusiness()
