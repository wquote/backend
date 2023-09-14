
from app import repositories
from app.services.base import BaseService


class DeckingCatalogStructuralService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_structural = DeckingCatalogStructuralService(repositories.decking_catalog_structural)
