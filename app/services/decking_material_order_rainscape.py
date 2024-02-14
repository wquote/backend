from app import repositories
from app.services.base import BaseService


repository = repositories.decking_material_order_rainscape

decking_material_order_rainscape = BaseService(repository)
