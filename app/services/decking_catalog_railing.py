
from app.models.catalog import Catalog
from app.services.base import BaseService

collection = 'decking_railing_catalogs'

decking_catalog_railing = BaseService(collection, Catalog)