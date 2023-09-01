
from app.models.catalog import Catalog
from app.services.base import BaseService

collection = 'decking_board_catalogs'

decking_catalog_board = BaseService(collection, Catalog)
