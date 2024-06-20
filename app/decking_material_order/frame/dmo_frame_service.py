from app.decking_quote.decking_quote_model import Layout
from app.shared.dmo_service import DeckingMaterialOrderSpecService
from app.shared.material_order_model import MaterialOrderSpecs

from .dmo_frame_repository import dmo_frame_repository


class DeckingMaterialOrderFrameService(DeckingMaterialOrderSpecService):
    def __init__(self, repository):
        super().__init__(repository)

    def estimate_material_order(self, layout: Layout | None) -> MaterialOrderSpecs:
        return super().estimate_material_order(layout)

dmo_frame_service = DeckingMaterialOrderFrameService(dmo_frame_repository)