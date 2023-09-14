
from app import repositories
from app.services.base import BaseService


class DeckingCatalogFinishingService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_finishing = DeckingCatalogFinishingService(repositories.decking_catalog_finishing)
