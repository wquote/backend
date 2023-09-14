
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_pt_frame_catalogs'
entity = Catalog

decking_catalog_pt_frame = BaseRepository(collection, entity)
