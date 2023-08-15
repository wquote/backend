
from app.models.decking_quote import DeckingQuote
from app.services.base import BaseService

collection = 'quotes'


decking_quote = BaseService(collection, DeckingQuote)
