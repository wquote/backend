from app.models.material_order import MaterialOrder
from app.repositories.base import BaseRepository

collection = "decking_material_order_rainscape"
entity = MaterialOrder

decking_material_order_rainscape = BaseRepository(collection, entity)
