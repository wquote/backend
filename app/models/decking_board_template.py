
from typing import List

from app.models.base import AppBaseModel


class DeckingBoardTempplateMaterial(AppBaseModel):
    id: str
    is_default: bool


class DeckingBoardTemplateBase(AppBaseModel):
    name: str | None = None
    materials: List[DeckingBoardTempplateMaterial] | None = None


class DeckingBoardTemplate(DeckingBoardTemplateBase):
    id: str


class DeckingBoardTemplateCreate(DeckingBoardTemplateBase):
    pass


class DeckingBoardTemplateUpdate(DeckingBoardTemplateBase):
    pass
