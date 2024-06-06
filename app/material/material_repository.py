from app.material.material_models import Material
from app.shared.base_repository import BaseRepository

collection = "materials"
entity = Material


class MaterialRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


material_repository: MaterialRepository = MaterialRepository(collection, entity)
