from app.shared.material_order_model import MaterialOrderSpecs
from .base_service import BaseService


class DeckingMaterialOrderSpec(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    # def estimate_material_order(self) -> MaterialOrderSpecs:

    #     aux = MaterialOrderSpecs()
    #     return aux
