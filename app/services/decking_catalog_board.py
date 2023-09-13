
from app import repositories
from app.services.base import BaseBusiness


class DeckingBoardCatalog(BaseBusiness):
    pass


decking_catalog_board = DeckingBoardCatalog(repositories.decking_catalog_board)
