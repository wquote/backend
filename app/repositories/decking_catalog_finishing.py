
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_finishing_catalogs'

decking_catalog_finishing = BaseRepository(collection, Catalog)
