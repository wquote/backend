
from typing import List

from app.models.base import AppBaseModel


class CatalogMaterialSpec(AppBaseModel):
    desc_snapshot: str = ''
    price_snapshot: float = 0.0
    qty: float = 0.0


class CatalogItemSpec(AppBaseModel):
    name: str | None = None
    materials: List[CatalogMaterialSpec] | None = None
    tax: float | None = None
    cost: float | None = None


class CatalogSpecs(AppBaseModel):
    selected_spec_index: int | None = None
    catalogs_spec: List[CatalogItemSpec] | None = None


class CatalogMaterial(AppBaseModel):
    id: str
    is_default: bool


class CatalogBase(AppBaseModel):
    name: str | None = None
    materials: List[CatalogMaterial] | None = None


class Catalog(CatalogBase):
    id: str


class CatalogCreate(CatalogBase):
    pass


class CatalogUpdate(CatalogBase):
    pass
