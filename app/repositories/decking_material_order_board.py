from app.models.material_order import MaterialOrder
from app.repositories.base import BaseRepository

collection = "decking_material_order_board"
entity = MaterialOrder

decking_material_order_board = BaseRepository(collection, entity)
