from app.shared.material_order_model import MaterialOrder
from app.shared.base_repository import BaseRepository

collection = "decking_material_order_galvanized"
entity = MaterialOrder


class DeckingMaterialOrderGalvanizedRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


dmo_galvanized_repository = DeckingMaterialOrderGalvanizedRepository(collection, entity)
