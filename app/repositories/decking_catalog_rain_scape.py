
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_rain_scape_catalogs'

decking_catalog_rain_scape = BaseRepository(collection, Catalog)
