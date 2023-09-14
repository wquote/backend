from app.models.material import Material
from app.repositories.base import BaseRepository

material: BaseRepository = BaseRepository('materials', Material)
