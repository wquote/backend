from app.shared.base_repository import BaseRepository
from app.shared.material_order_model import MaterialOrder

collection = "decking_material_order_railing"
entity = MaterialOrder


class DeckingMaterialOrderRailingRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


dmo_railing_repository = DeckingMaterialOrderRailingRepository(collection, entity)

