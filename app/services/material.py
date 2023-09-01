from app.models.material import Material
from app.services.base import BaseService

material: BaseService = BaseService('materials', Material)
