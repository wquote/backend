
from app.models.catalog import Catalog
from app.services.base import BaseService

collection = 'decking_finishing_catalogs'

decking_catalog_finishing = BaseService(collection, Catalog)
