from datetime import datetime
from typing import List

from fastapi import HTTPException

from app.decking_quote.decking_quote_model import (
    DeckTakeOff,
    DeckingMaterialOrderSpecs,
    DeckingQuoteBase,
    DeckingQuoteCreate,
    DeckingQuoteUpdate,
    Footings,
)
from app.decking_quote.decking_quote_repository import decking_quote_repository
from app.material.material_service import material_service
from app.shared.base_service import BaseService
from app.shared.material_order_model import (
    MaterialOrder,
    MaterialOrderSpec,
    MaterialOrderSpecItem,
    MaterialOrderSpecs,
)
from app.utils import randomFloat

from app.decking_material_order.footing.dmo_footing_service import dmo_footing_service
from app.decking_material_order.frame.dmo_frame_service import dmo_frame_service
from app.decking_material_order.galvanized.dmo_galvanized_service import (
    dmo_galvanized_service,
)
from app.decking_material_order.board.dmo_board_service import dmo_board_service
from app.decking_material_order.railing.dmo_railing_service import dmo_railing_service
from app.decking_material_order.finishing.dmo_finishing_service import (
    dmo_finishing_service,
)
from app.decking_material_order.rain_scape.dmo_rain_scape_service import (
    dmo_rain_scape_service,
)

from app.shared import dmo_service


class DeckingQuoteService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    from fastapi import HTTPException

    def create(self, item: DeckingQuoteCreate) -> str:
        """
        Creates a new decking quote.

        Args:
            item (DeckingQuoteCreate): The decking quote data.

        Returns:
            str: The ID of the inserted decking quote.

        Raises:
            HTTPException: If the insertion failed.
        """

        self.update_dates(item)

        item.material_order = self.create_material_order(item.deck_take_off)

        inserted_id = decking_quote_repository.create(item)
        if not inserted_id:
            raise HTTPException(status_code=400, detail="Insertion failed")

        return inserted_id

    def update(self, id: str, item: DeckingQuoteUpdate) -> bool:
        self.update_dates(item)

        if decking_quote_repository.update(id, item):
            return True

        return False

    def update_dates(self, item: DeckingQuoteBase) -> None:
        item.updated_at = datetime.now()
        if item.created_at is None:
            item.created_at = item.updated_at

    def create_material_order(self, deck_take_off: DeckTakeOff | None) -> DeckingMaterialOrderSpecs:
        dmo_specs: DeckingMaterialOrderSpecs = DeckingMaterialOrderSpecs()

        if not deck_take_off:
            return dmo_specs

        dmo_footings_specs: MaterialOrderSpecs = dmo_footing_service.estimate_material_order(deck_take_off.footings)
        dmo_frame_specs: MaterialOrderSpecs = dmo_frame_service.estimate_material_order(deck_take_off.layout)

        # decking_quote.profit = randomFloat(3000, 5000)
        # decking_quote.value = randomFloat(15000, 30000)

        dmo_specs = DeckingMaterialOrderSpecs(
            footings=dmo_footings_specs,
            frame=dmo_frame_specs,
            galvanized=None,
            board=None,
            railing=None,
            finishing=None,
            rain_scape=None,
        )

        return dmo_specs

    def update_material_order(self, id: str, decking_quote: DeckingQuoteUpdate):
        decking_quote.material_order = self.create_material_order(decking_quote.deck_take_off)

        return self.update(id, decking_quote)


decking_quote_service = DeckingQuoteService(decking_quote_repository)
