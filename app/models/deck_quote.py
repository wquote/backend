
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from app.models.quote import QuoteModel, QuoteUpdateModel
from app.utils import generate_uuid4


class Area(BaseModel):
    width: float
    depth: float


class Stair(BaseModel):
    width: float
    riser: float


class DeckModel(BaseModel):
    main_areas: List[Area]
    lading_areas: List[Area] | None
    stairs: List[Stair] | None


class DeckUpdateModel(BaseModel):
    main_areas: List[Area] | None
    lading_areas: List[Area] | None
    stairs: List[Stair] | None


class DeckBoardSpecMaterialModel(BaseModel):
    id: str
    desc: str
    qty: float
    price_snapshot: float


class DeckBoardSpecification(BaseModel):
    id_deckboard_template: str
    name: str
    materials: List[DeckBoardSpecMaterialModel]
    tax: float
    cost: float


class DeckQuoteModel(QuoteModel):
    deck: DeckModel
    board_specs: List[DeckBoardSpecification] | None


class DeckQuoteCreateModel(DeckQuoteModel):
    id: str = Field(default_factory=lambda: generate_uuid4())


class DeckQuoteUpdateModel(QuoteUpdateModel):
    deck: DeckModel | None
    board_specs: List[DeckBoardSpecification] | None
