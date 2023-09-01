
from app.models.catalog import Catalog
from app.services.base import BaseService

collection = 'decking_structural_catalogs'

decking_catalog_structural = BaseService(collection, Catalog)
