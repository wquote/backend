from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_finishing

decking_material_order_finishing = BaseService(repository)
