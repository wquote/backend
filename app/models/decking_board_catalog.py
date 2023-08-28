
from typing import List

from app.models.base import AppBaseModel


class DeckingBoardCatalogMaterial(AppBaseModel):
    id: str
    is_default: bool


class DeckingBoardCatalogBase(AppBaseModel):
    name: str | None = None
    materials: List[DeckingBoardCatalogMaterial] | None = None


class DeckingBoardCatalog(DeckingBoardCatalogBase):
    id: str


class DeckingBoardCatalogCreate(DeckingBoardCatalogBase):
    pass


class DeckingBoardCatalogUpdate(DeckingBoardCatalogBase):
    pass
