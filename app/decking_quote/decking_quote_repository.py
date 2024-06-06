from app.shared.base_repository import BaseRepository

from .decking_quote_models import DeckingQuote

collection = "quotes"
entity = DeckingQuote


class DeckingQuoteRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


decking_quote_repository: DeckingQuoteRepository = DeckingQuoteRepository(collection, entity)
