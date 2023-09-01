
from app import services
from app.business.base import BaseBusiness


class DeckingBoardCatalog(BaseBusiness):
    pass


decking_catalog_board = DeckingBoardCatalog(services.decking_catalog_board)
