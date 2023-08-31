
from app.models.catalog import Catalog
from app.services.base import BaseService


collection = 'decking_railing_catalogs'

decking_railing_catalog = BaseService(collection, Catalog)
