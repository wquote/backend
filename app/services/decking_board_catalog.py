

from app.models.decking_board_catalog import DeckingBoardCatalog
from app.services.base import BaseService


collection = 'decking_board_catalogs'

decking_board_catalog = BaseService(collection, DeckingBoardCatalog)
