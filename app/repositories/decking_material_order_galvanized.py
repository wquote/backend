from app.models.material_order import MaterialOrder
from app.repositories.base import BaseRepository

collection = "decking_material_order_galvanized"
entity = MaterialOrder

decking_material_order_galvanized = BaseRepository(collection, entity)
