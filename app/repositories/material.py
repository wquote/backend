
from app.models.material import Material
from app.repositories.base import BaseRepository

collection = 'materials'
entity = Material

material: BaseRepository = BaseRepository(collection, entity)
