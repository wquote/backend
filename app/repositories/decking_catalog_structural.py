
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_structural_catalogs'

decking_catalog_structural = BaseRepository(collection, Catalog)
