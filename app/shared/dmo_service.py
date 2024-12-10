from typing import List

from app.decking_quote.decking_quote_model import Footings, Layout
from app.material.material_models import Material
from app.material.material_service import material_service

# functions used by 'eval()'. don't delete
from app.shared.dmo_estimate_formulas.frame_formulas import estimate_frame_material
from app.shared.dmo_estimate_formulas.galvanized_formulas import *

from app.shared.material_order_model import MaterialOrder, MaterialOrderSpec, MaterialOrderSpecItem, MaterialOrderSpecs

from .base_service import BaseService


class DeckingMaterialOrderSpecService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def estimate_material_order(self, deck_take_off_item) -> MaterialOrderSpecs:
        # Create a new MaterialOrder specification
        dmo_specs: MaterialOrderSpecs = MaterialOrderSpecs()

        # If there are no footings, return an empty MaterialOrderSpecs
        if not deck_take_off_item:
            return dmo_specs

        # Necessary to eval() work properly
        if isinstance(deck_take_off_item, Footings):
            footings: Footings = deck_take_off_item
        if isinstance(deck_take_off_item, Layout):
            layout: Layout = deck_take_off_item

        dmo_specs.selected_spec_index = 0
        dmo_specs.material_order_specs = []
        
        # Read all decking material order specs (sheets)
        dmot_list: List[MaterialOrder] = self.read_all()

        for dmot in dmot_list:
            dmo_specs.material_order_specs.append(
                MaterialOrderSpec(
                    name=dmot.name,
                    materials=[],
                    tax=0.0,
                    cost=0.0,
                )
            )

            # Read all materials in the material order template
            for mot_material in dmot.materials if dmot.materials is not None else []:
                formula: str | None = mot_material.formula
                estimated_qty: float = eval(formula if formula else "0")
                material: Material = material_service.read(mot_material.id)

                if dmo_specs.material_order_specs[-1].materials is not None:
                    dmo_specs.material_order_specs[-1].materials.append(
                        MaterialOrderSpecItem(
                            reference_snapshot=material.reference if material.reference else "",
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

        return dmo_specs
