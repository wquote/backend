from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_railing

decking_material_order_railing = BaseService(repository)
