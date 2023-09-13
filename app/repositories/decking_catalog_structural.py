
from app.models.catalog import Catalog
from app.repositories.base import BaseService

collection = 'decking_structural_catalogs'

decking_catalog_structural = BaseService(collection, Catalog)
