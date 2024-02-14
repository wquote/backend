from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_footings

decking_material_order_footings = BaseService(repository)
