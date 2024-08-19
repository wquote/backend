from app.shared.dmo_repository import DmoRepository
from app.shared.material_order_model import MaterialOrderDTO

collection = "decking_material_order_footings"
entity = MaterialOrderDTO


class DeckingMaterialOrderFootingRepository(DmoRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


dmo_footing_repository = DeckingMaterialOrderFootingRepository(collection, entity)
