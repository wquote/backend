
from app import repositories
from app.services.base import BaseService


class DeckingBoardCatalogService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_board = DeckingBoardCatalogService(repositories.decking_catalog_board)
