
from app import repositories
from app.services.base import BaseService


class DeckingCatalogRainScapeService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_rain_scape = DeckingCatalogRainScapeService(repositories.decking_catalog_rain_scape)
