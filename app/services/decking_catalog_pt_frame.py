
from app import repositories
from app.services.base import BaseService


class DeckingPTFrameCatalogService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


decking_catalog_pt_frame = DeckingPTFrameCatalogService(repositories.decking_catalog_pt_frame)
