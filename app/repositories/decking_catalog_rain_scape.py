
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_rain_scape_catalogs'
entity = Catalog

decking_catalog_rain_scape = BaseRepository(collection, entity)
