from typing import Any, List
from app.decking_quote.decking_quote_models import DeckTakeOff, Footings
from app.material.material_models import Material
from app.shared.base_service import BaseService
from app.shared.material_order_model import MaterialOrder, MaterialOrderSpec, MaterialOrderSpecItem, MaterialOrderSpecs
from app.material.material_service import material_service

from .dmo_footing_repository import dmo_footing_repository

repository = dmo_footing_repository


class DeckingMaterialOrderFootingService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def estimate_material_order(self, footings: Footings | None) -> MaterialOrderSpecs:
        # Create a new MaterialOrder specification
        dmo_specs: MaterialOrderSpecs = MaterialOrderSpecs()

        # If there are no footings, return an empty MaterialOrderSpecs
        if not footings:
            return dmo_specs

        dmo_specs.material_order_specs = []
        # Read all footings material order specs (sheets)
        mo_list: List[MaterialOrder] = self.read_all()

        #
        for mo in mo_list:
            dmo_specs.material_order_specs.append(
                MaterialOrderSpec(
                    name=mo.name,
                    materials=[],
                    tax=0.0,
                    cost=0.0,
                )
            )

            # Read all materials in the material order
            for mo_material in mo.materials if mo.materials is not None else []:
                formula: str | None = mo_material.formula
                estimated_qty: float = eval(formula if formula else "0")
                material: Material = material_service.read(mo_material.id)

                if dmo_specs.material_order_specs[-1].materials is not None:
                    dmo_specs.material_order_specs[-1].materials.append(
                        MaterialOrderSpecItem(
                            desc_snapshot=material.desc if material.desc else "",
                            price_snapshot=material.price if material.price else 0.0,
                            formula_snapshot=formula if formula else "",
                            estimated_qty=estimated_qty,
                            qty=estimated_qty,
                        )
                    )

            # Calculate the cost of the material order
            amount_sum: float = 0.0
            mo_spec_item: List[MaterialOrderSpecItem] | None = dmo_specs.material_order_specs[-1].materials
            for item in mo_spec_item if mo_spec_item is not None else []:
                amount_sum += item.qty * item.price_snapshot

            dmo_specs.material_order_specs[-1].tax = 0.0625 * amount_sum

            dmo_specs.material_order_specs[-1].cost = amount_sum + dmo_specs.material_order_specs[-1].tax

        dmo_specs.selected_spec_index = 0
        return dmo_specs

    # def update_material_order_estimated_qty(self, footings: Footings | None, mo_footings: MaterialOrderSpecs | None):
    #     if not footings or not mo_footings:
    #         return

    #     for mo in mo_footings.material_order_specs if mo_footings.material_order_specs else []:
    #         for mo_material in mo.materials if mo.materials else []:
    #             formula: str = mo_material.formula_snapshot
    #             estimated_qty: float = eval(formula if formula else "0")

    #             mo_material.estimated_qty = estimated_qty
    #             mo_material.qty = estimated_qty


dmo_footing_service = DeckingMaterialOrderFootingService(repository)
