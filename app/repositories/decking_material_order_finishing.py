from app.models.material_order import MaterialOrder
from app.repositories.base import BaseRepository

collection = "decking_material_order_finishing"
entity = MaterialOrder

decking_material_order_finishing = BaseRepository(collection, entity)
