
from app import repositories
from app.services.base import BaseService


class DeckingRailingCatalogService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_railing = DeckingRailingCatalogService(repositories.decking_catalog_railing)
