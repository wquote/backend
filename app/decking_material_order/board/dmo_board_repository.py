from app.shared.base_repository import BaseRepository
from app.shared.material_order_model import MaterialOrder

collection = "decking_material_order_board"
entity = MaterialOrder


class DeckingMaterialOrderBoardRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


dmo_board_repository = BaseRepository(collection, entity)
