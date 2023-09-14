
from app.models.decking_quote import DeckingQuote
from app.repositories.base import BaseRepository

collection = 'quotes'


decking_quote = BaseRepository(collection, DeckingQuote)
