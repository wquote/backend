from app import repositories
from app.services.base import BaseService


respository = repositories.decking_material_order_board

decking_material_order_board = BaseService(respository)
