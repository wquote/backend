from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_frame

decking_material_order_frame = BaseService(repository)
