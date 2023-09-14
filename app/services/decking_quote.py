from datetime import datetime
from typing import List

from app import repositories, services
from app.models.catalog import (Catalog, CatalogItemSpec, CatalogMaterialSpec,
                                CatalogSpecs)
from app.models.decking_quote import (DeckingQuoteBase, DeckingQuoteCreate,
                                      DeckingQuoteUpdate)
from app.services.base import BaseService
from app.utils import randomFloat


class DeckingQuoteService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def create(self, item: DeckingQuoteCreate) -> str | None:
        estimated_item = self.estimate(item)

        if (inserted_id := repositories.decking_quote.create(estimated_item)):
            return inserted_id

        return None

    def update(self, id: str, item: DeckingQuoteUpdate) -> bool:
        processed_deck_quote_dict: dict = self.estimate(item).model_dump()
        processed_deck_quote = DeckingQuoteUpdate(**processed_deck_quote_dict)

        if (repositories.decking_quote.update(id, processed_deck_quote)):
            return True

        return False

    def estimate(self, decking_quote: DeckingQuoteBase) -> DeckingQuoteBase:

        decking_quote.updated_at = datetime.now()
        if decking_quote.created_at is None:
            decking_quote.created_at = decking_quote.updated_at

        self.update_catalog_specs(decking_quote, 'board_specs', services.decking_catalog_board)
        self.update_catalog_specs(decking_quote, 'railing_specs', services.decking_catalog_railing)
        self.update_catalog_specs(decking_quote, 'pressure_treated_specs', services.decking_catalog_pt_frame)
        self.update_catalog_specs(decking_quote, 'structural_specs', services.decking_catalog_structural)
        self.update_catalog_specs(decking_quote, 'finishing_specs', services.decking_catalog_finishing)
        self.update_catalog_specs(decking_quote, 'rain_scape_specs', services.decking_catalog_rain_scape)

        decking_quote.profit = randomFloat(3000, 5000)
        decking_quote.value = randomFloat(15000, 30000)

        return decking_quote

    def update_catalog_specs(self, decking_quote, specs_type, catalog_service):
        selected_spec_index = getattr(getattr(decking_quote, specs_type), 'selected_spec_index', 0)
        catalogs_exists = getattr(getattr(decking_quote, specs_type), 'catalogs_spec', None)

        if not catalogs_exists:
            catalogs = catalog_service.read_all()
            obj = {
                'selected_spec_index': selected_spec_index,
                'catalogs_spec': self.create_catalog_specs(catalogs)
            }
            setattr(decking_quote, specs_type, CatalogSpecs(**obj))

    def create_catalog_specs(self, catalogs: List[Catalog]) -> List[CatalogItemSpec]:
        # catalogs_spec
        catalog_specs: List[CatalogItemSpec] = []
        for catalog in catalogs:
            catalog_spec_name: str | None = catalog.name

            # catalog_materials_spec
            catalog_materials_spec: List[CatalogMaterialSpec] = []
            for catalog_material in catalog.materials if catalog.materials else []:
                qty: float | None = 0.0
                price_snapshot: float | None = 0.0
                desc: str | None = ''

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

                catalog_materials_spec.append(CatalogMaterialSpec(**obj))

            amount_sum: float = sum(material.price_snapshot * float(material.qty) for material in catalog_materials_spec)
            tax: float = 0.0625 * amount_sum
            cost: float = amount_sum + tax

            obj = dict(
                name=catalog_spec_name,
                materials=catalog_materials_spec,
                tax=tax,
                cost=cost
            )

            catalog_specs.append(CatalogItemSpec(**obj))

        return catalog_specs


decking_quote = DeckingQuoteService(repositories.decking_quote)
