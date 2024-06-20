# from datetime import datetime
from typing import Any, List

from app.quote.quote_model import Quote, QuoteBase, QuoteCreate
from app.shared.base_model import AppBaseModel
from app.shared.material_order_model import MaterialOrderSpecs

# from pydantic import Field


class DescCost(AppBaseModel):
    desc: str | None = None
    cost: float | None = None


class DescQtyCost(AppBaseModel):
    desc: str | None = None
    qty: float | None = None
    cost: float | None = None


class QtySize(AppBaseModel):
    qty: float | None = None
    size: str | None = None


class Area(AppBaseModel):
    deck_grade: str | None = None
    ledger_board: QtySize | None = None
    ledger_attaches_to: str | None = None
    support_post_grade: QtySize | None = None
    width: float | None = None
    depth: float | None = None
    height: float | None = None
    picture_frame: float | None = None
    beam_grade: QtySize | None = None


class Stair(AppBaseModel):
    width: float | None = None
    riser: float | None = None
    support_post_grade: QtySize | None = None
    beam_grade: QtySize | None = None
    railings_on: str | None = None


class Layout(AppBaseModel):
    main_areas: List[Area] | None = None
    lading_areas: List[Area] | None = None
    stairs: List[Stair] | None = None


class Footings(AppBaseModel):
    big_foot: QtySize | None = None
    helical_post: QtySize | None = None
    sonotube: QtySize | None = None


class DeckTakeOff(AppBaseModel):
    footings: Footings | None = None
    layout: Layout | None = None
    railing: List[Any] | None = None
    finishing: List[Any] | None = None
    rains_cape: List[Any] | None = None


class DeckingMaterialOrderSpecs(AppBaseModel):
    footings: MaterialOrderSpecs | None = None
    frame: MaterialOrderSpecs | None = None
    galvanized: MaterialOrderSpecs | None = None
    board: MaterialOrderSpecs | None = None
    railing: MaterialOrderSpecs | None = None
    finishing: MaterialOrderSpecs | None = None
    rain_scape: MaterialOrderSpecs | None = None
    extra_materials: List[DescQtyCost] | None = None


class DeckingQuoteBase(QuoteBase):
    deck_take_off: DeckTakeOff | None = None
    material_order: DeckingMaterialOrderSpecs | None = None
    labor_costs: List[DescCost] | None = None
    other_costs: List[DescQtyCost] | None = None


class DeckingQuote(Quote, DeckingQuoteBase):
    pass


class DeckingQuoteCreate(QuoteCreate, DeckingQuoteBase):
    pass


class DeckingQuoteUpdate(DeckingQuoteBase):
    pass
