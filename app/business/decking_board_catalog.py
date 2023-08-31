
from app import services
from app.business.base import BaseBusiness


class DeckingBoardCatalog(BaseBusiness):
    pass


decking_board_catalog = DeckingBoardCatalog(services.decking_board_catalog)
