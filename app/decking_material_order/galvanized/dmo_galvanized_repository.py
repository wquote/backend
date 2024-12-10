from app.shared.dmo_repository import DmoRepository
from app.shared.material_order_model import MaterialOrderDTO

collection = "decking_material_order_galvanized"
dto = MaterialOrderDTO


class DeckingMaterialOrderGalvanizedRepository(DmoRepository):
    def __init__(self, collection: str, dto):
        super().__init__(collection, dto)


dmo_galvanized_repository = DeckingMaterialOrderGalvanizedRepository(collection, dto)
