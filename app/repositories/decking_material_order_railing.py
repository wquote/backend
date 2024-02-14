from app.models.material_order import MaterialOrder
from app.repositories.base import BaseRepository

collection = "decking_material_order_railing"
entity = MaterialOrder

decking_material_order_railing = BaseRepository(collection, entity)
