
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_board_catalogs'
entity = Catalog

decking_catalog_board = BaseRepository(collection, entity)
