from app.shared.base_repository import BaseRepository
from app.shared.material_order_model import MaterialOrder

collection = "decking_material_order_rainscape"
entity = MaterialOrder


class DeckingMaterialOrderRainScapeRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


dmo_rain_scape_repository = DeckingMaterialOrderRainScapeRepository(collection, entity)
