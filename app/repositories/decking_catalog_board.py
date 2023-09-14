
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_board_catalogs'

decking_catalog_board = BaseRepository(collection, Catalog)
