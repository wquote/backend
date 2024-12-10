from typing import List

from app.shared.base_model import AppBaseModel


# MaterialOrderSpecs = footings, frame, galvanized strap, decking board, railing sysyem, finishing, rain scape, extra materials


# Especificação da lista de pedido de materiais para a cotacao
class MaterialOrderSpecItem(AppBaseModel):
    reference_snapshot: str = ""
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
# Template de lista de pedido de materiais
class MaterialOrderItem(AppBaseModel):
    id: str
    formula: str | None = None
    group_order: int | None = None # field to sort materials do to be estimated


class MaterialOrderItemDTO(MaterialOrderItem):
    name: str | None = None


class MaterialOrderBase(AppBaseModel):
    name: str | None = None
    materials: List[MaterialOrderItem] | None = None


class MaterialOrder(MaterialOrderBase):
    id: str


class MaterialOrderDTO(MaterialOrderBase):
    id: str
    materials: List[MaterialOrderItemDTO] | None = None


class MaterialOrderCreate(MaterialOrderBase):
    pass


class MaterialOrderUpdate(MaterialOrderBase):
    pass
