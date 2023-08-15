
from datetime import datetime
from typing import Any, List

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.quote import Quote, QuoteBase, QuoteCreate


class Area(AppBaseModel):
    width: float | None = None
    depth: float | None = None
    height: float | None = None


class Stair(AppBaseModel):
    width: float | None = None
    riser: float | None = None


class Decking(AppBaseModel):
    main_areas: List[Area] | None = None
    lading_areas: List[Area] | None = None
    stairs: List[Stair] | None = None


class DeckingBoardSpecMaterial(AppBaseModel):
    desc_snapshot: str | None = None
    price_snapshot: float
    qty: float


class DeckingBoardSpec(AppBaseModel):
    name: str | None = None
    materials: List[DeckingBoardSpecMaterial] | None = None
    tax: float | None = None
    cost: float | None = None


class DeckingQuoteBase(QuoteBase):
    decking: Decking | None = None
    pressure_treated: List[Any] | None = None
    structural: List[Any] | None = None
    decking_board_specs: List[DeckingBoardSpec] | None = None
    railling_specs: List[Any] | None = None
    rain_scape_specs: List[Any] | None = None
    finishing: List[Any] | None = None
    extras: List[Any] | None = None


class DeckingQuote(Quote, DeckingQuoteBase):
    pass


class DeckingQuoteCreate(QuoteCreate, DeckingQuoteBase):
    pass


class DeckingQuoteUpdate(DeckingQuoteBase):
    pass
