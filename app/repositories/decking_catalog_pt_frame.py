
from app.models.catalog import Catalog
from app.repositories.base import BaseService

collection = 'decking_pt_frame_catalogs'

decking_catalog_pt_frame = BaseService(collection, Catalog)
