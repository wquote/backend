from app.models.material import Material, MaterialCreate, MaterialUpdate
from app.services.base import BaseService

material = BaseService('materials', Material)
