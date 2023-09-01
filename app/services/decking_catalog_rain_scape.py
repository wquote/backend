
from app.models.catalog import Catalog
from app.services.base import BaseService

collection = 'decking_rain_scape_catalogs'

decking_catalog_rain_scape = BaseService(collection, Catalog)
