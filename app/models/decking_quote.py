
from datetime import datetime
from typing import Any, List

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.catalog import CatalogSpecs
from app.models.quote import Quote, QuoteBase, QuoteCreate


class Area(AppBaseModel):
    width: float | None = None
    depth: float | None = None
    height: float | None = None


class Stair(AppBaseModel):
    width: float | None = None
    riser: float | None = None


class DeckingInfo(AppBaseModel):
    main_areas: List[Area] | None = None
    lading_areas: List[Area] | None = None
    stairs: List[Stair] | None = None


class DeckingQuoteBase(QuoteBase):
    decking_info: DeckingInfo | None = None
    pressure_treated: List[Any] | None = None
    structural: List[Any] | None = None
    board_specs: CatalogSpecs | None = None
    railing_specs: CatalogSpecs | None = None
    rain_scape_specs: CatalogSpecs | None = None
    finishing: List[Any] | None = None
    extras: List[Any] | None = None


class DeckingQuote(Quote, DeckingQuoteBase):
    pass


class DeckingQuoteCreate(QuoteCreate, DeckingQuoteBase):
    pass


class DeckingQuoteUpdate(DeckingQuoteBase):
    pass
