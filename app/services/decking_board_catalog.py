
from app.models.catalog import Catalog
from app.services.base import BaseService


collection = 'decking_board_catalogs'

decking_board_catalog = BaseService(collection, Catalog)