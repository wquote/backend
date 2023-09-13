from app.models.material import Material
from app.repositories.base import BaseService

material: BaseService = BaseService('materials', Material)
