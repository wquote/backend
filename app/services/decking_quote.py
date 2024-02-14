from datetime import datetime
from typing import List

from app import repositories, services
from app.models.material_order import (
    MaterialOrder,
    MaterialOrderSpec,
    MaterialOrderSpecItem,
    MaterialOrderSpecs,
)
from app.models.decking_quote import (
    DeckingMaterialOrder,
    DeckingQuoteBase,
    DeckingQuoteCreate,
    DeckingQuoteUpdate,
)
from app.services.base import BaseService
from app.utils import randomFloat


class DeckingQuoteService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def create(self, item: DeckingQuoteCreate) -> str | None:
        estimated_item = self.estimate(item)

        if inserted_id := repositories.decking_quote.create(estimated_item):
            return inserted_id

        return None

    def update(self, id: str, item: DeckingQuoteUpdate) -> bool:
        processed_deck_quote_dict: dict = self.estimate(item).model_dump()
        processed_deck_quote = DeckingQuoteUpdate(**processed_deck_quote_dict)

        if repositories.decking_quote.update(id, processed_deck_quote):
            return True

        return False

    def estimate(self, decking_quote: DeckingQuoteBase) -> DeckingQuoteBase:
        decking_quote.updated_at = datetime.now()
        if decking_quote.created_at is None:
            decking_quote.created_at = decking_quote.updated_at

        self.create_material_order_specs_if_not_exists(decking_quote, "footings", services.decking_material_order_footings)
        self.create_material_order_specs_if_not_exists(decking_quote, "frame", services.decking_material_order_frame)
        self.create_material_order_specs_if_not_exists(decking_quote, "galvanized", services.decking_material_order_galvanized)
        self.create_material_order_specs_if_not_exists(decking_quote, "board", services.decking_material_order_board)
        self.create_material_order_specs_if_not_exists(decking_quote, "railing", services.decking_material_order_railing)
        self.create_material_order_specs_if_not_exists(decking_quote, "finishing", services.decking_material_order_finishing)
        self.create_material_order_specs_if_not_exists(decking_quote, "rain_scape", services.decking_material_order_rainscape)

        decking_quote.profit = randomFloat(3000, 5000)
        decking_quote.value = randomFloat(15000, 30000)

        return decking_quote

    def create_material_order_specs_if_not_exists(self, decking_quote: DeckingQuoteBase, specs_type: str, material_order_service: BaseService):
        material_order_spec_exists: bool = (
            getattr(decking_quote, "material_order", None)
            and getattr(decking_quote.material_order, specs_type, None)
            and getattr(getattr(decking_quote.material_order, specs_type), "material_order_specs", None)
        ) or False

        # If not exists, create
        if not material_order_spec_exists:
            # access the selected_spec_index. if not exists, attribute 0 to index variable
            index: int = (
                getattr(decking_quote, "material_order", None)
                and getattr(decking_quote.material_order, specs_type, None)
                and getattr(getattr(decking_quote.material_order, specs_type), "selected_spec_index", None)
            ) or 0

            templates: List[MaterialOrder] = material_order_service.read_all()
            obj: dict = {
                "selected_spec_index": index,
                "material_order_specs": self.create_material_order_specs(templates),
            }

            if not getattr(decking_quote, "material_order", None):
                decking_quote.material_order = DeckingMaterialOrder()
                
            setattr(decking_quote.material_order, specs_type, MaterialOrderSpecs(**obj))

    def create_material_order_specs(self, material_orders: List[MaterialOrder]) -> List[MaterialOrderSpec]:
        # catalogs_spec
        material_order_specs: List[MaterialOrderSpec] = []
        for material_order in material_orders:
            catalog_spec_name: str | None = material_order.name

            # catalog_materials_spec
            catalog_materials_spec: List[MaterialOrderSpecItem] = []
            for catalog_material in material_order.materials if material_order.materials else []:
                qty: float | None = 0.0
                price_snapshot: float | None = 0.0
                desc: str | None = ""

                if material := services.material.read(catalog_material.id):
                    price_snapshot = material.price
                    desc = material.desc

                    if catalog_material.is_default:
                        qty = randomFloat(1, 10)

                obj: dict = {
                    "desc_snapshot": desc,
                    "price_snapshot": price_snapshot,
                    "qty": qty,
                }

                catalog_materials_spec.append(MaterialOrderSpecItem(**obj))

            amount_sum: float = sum(material.price_snapshot * float(material.qty) for material in catalog_materials_spec)
            tax: float = 0.0625 * amount_sum
            cost: float = amount_sum + tax

            obj = {
                "name": catalog_spec_name,
                "materials": catalog_materials_spec,
                "tax": tax,
                "cost": cost,
            }

            material_order_specs.append(MaterialOrderSpec(**obj))

        return material_order_specs


decking_quote = DeckingQuoteService(repositories.decking_quote)
