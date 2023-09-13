
from app import repositories
from app.services.base import BaseBusiness


class DeckingPTFrameCatalog(BaseBusiness):
    pass


decking_catalog_pt_frame = DeckingPTFrameCatalog(repositories.decking_catalog_pt_frame)
