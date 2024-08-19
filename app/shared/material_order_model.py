from typing import List

from app.shared.base_model import AppBaseModel


# MaterialOrderSpecs = footings, frame, galvanized strap, decking board, railing sysyem, finishing, rain scape, extra materials


# Snapshot da lista de pedido de materiais para a cotacao
class MaterialOrderSpecItem(AppBaseModel):
    desc_snapshot: str = ""
    price_snapshot: float = 0.0
    formula_snapshot: str = ""
    estimated_qty: float = 0.0
    qty: float = 0.0


class MaterialOrderSpec(AppBaseModel):
    name: str | None = None
    materials: List[MaterialOrderSpecItem] | None
    tax: float | None = None
    cost: float | None = None


class MaterialOrderSpecs(AppBaseModel):
    selected_spec_index: int | None = None
    material_order_specs: List[MaterialOrderSpec] | None = None


# ###############################################
# Lista de pedido de materiais editavel pelo admin
class MaterialOrderItem(AppBaseModel):
    id: str
    formula: str | None = None


class MaterialOrderBase(AppBaseModel):
    name: str | None = None
    materials: List[MaterialOrderItem] | None = None


class MaterialOrder(MaterialOrderBase):
    id: str


class MaterialOrderCreate(MaterialOrderBase):
    pass


class MaterialOrderUpdate(MaterialOrderBase):
    pass


class MaterialOrderSpecItemDTO(MaterialOrderItem):
    name: str | None = None


class MaterialOrderDTO(MaterialOrderBase):
    id: str
    materials: List[MaterialOrderSpecItemDTO] | None = None
