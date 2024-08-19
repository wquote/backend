from typing import Any, List

from app.decking_quote.decking_quote_model import DeckTakeOff, Footings
from app.material.material_models import Material
from app.material.material_service import material_service
from app.shared.dmo_service import DeckingMaterialOrderSpecService
from app.shared.material_order_model import MaterialOrder, MaterialOrderSpec, MaterialOrderSpecItem, MaterialOrderSpecs

from .dmo_footing_repository import dmo_footing_repository

repository = dmo_footing_repository


class DeckingMaterialOrderFootingService(DeckingMaterialOrderSpecService):

    def __init__(self, repository):
        super().__init__(repository)

    # footings parameter is used in eva(formula)
    def estimate_material_order(self, footings: Footings | None) -> MaterialOrderSpecs:
        return super().estimate_material_order(footings)


dmo_footing_service = DeckingMaterialOrderFootingService(repository)
