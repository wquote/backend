
from app import repositories
from app.services.base import BaseBusiness


class DeckingRailingCatalog(BaseBusiness):
    pass


decking_catalog_railing = DeckingRailingCatalog(repositories.decking_catalog_railing)
