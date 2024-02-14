from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_galvanized

decking_material_order_galvanized = BaseService(repository)
