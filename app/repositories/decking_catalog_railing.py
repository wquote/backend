
from app.models.catalog import Catalog
from app.repositories.base import BaseRepository

collection = 'decking_railing_catalogs'
entity = Catalog

decking_catalog_railing = BaseRepository(collection, entity)
