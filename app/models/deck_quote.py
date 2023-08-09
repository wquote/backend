
from datetime import datetime
from typing import Annotated, List
from bson import ObjectId

from pydantic import Field

from app.models.base import AppBaseModel, PyObjectId
from app.models.quote import Quote, QuoteBase, QuoteCreate


class Area(AppBaseModel):
    width: float
    depth: float
    height: float


class Stair(AppBaseModel):
    width: float
    riser: float


class Deck(AppBaseModel):
    main_areas: List[Area]
    lading_areas: List[Area] | None = None
    stairs: List[Stair] | None = None


class DeckBoardSpecMaterial(AppBaseModel):
    id: str
    name_snapshot: str
    price_snapshot: float
    qty: float


class DeckBoardSpecification(AppBaseModel):
    id_deckboard_template: str
    name: str
    materials: List[DeckBoardSpecMaterial]
    tax: float
    cost: float


class DeckQuoteBase(QuoteBase):
    deck: Deck | None = None
    # board_specifications: List[DeckBoardSpecification] | None = None


class DeckQuote(Quote, DeckQuoteBase):
    pass


class DeckQuoteCreate(QuoteCreate, DeckQuoteBase):
    deck: Deck


class DeckQuoteUpdate(DeckQuoteBase):
    pass


class DeckQuoteInDB(DeckQuoteBase):
    id: Annotated[ObjectId, PyObjectId] = Field(default_factory=ObjectId, alias='_id')

    class Config:
        json_encoders = {ObjectId: str}
