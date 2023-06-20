
from typing import List

from pydantic import BaseModel, Field

from app.utils import generate_uuid4


class DeckBoardTempplateMaterialModel(BaseModel):
    id: str
    is_default: bool


class DeckBoardTemplateModel(BaseModel):
    id: str
    name: str
    materials: List[DeckBoardTempplateMaterialModel]


class DeckBoardTemplateCreateModel(DeckBoardTemplateModel):
    id: str = Field(default_factory=lambda: generate_uuid4())


class DeckBoardTemplateUpdateModel(BaseModel):
    pass
