
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_finishing_catalogs'
entity = Catalog

decking_catalog_finishing = BaseRepository(collection, entity)
