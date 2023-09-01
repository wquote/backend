from datetime import datetime
from typing import List

from app import business, services
from app.models.catalog import CatalogItemSpec, CatalogMaterialSpec, CatalogSpecs
from app.models.catalog import Catalog
from app.models.decking_quote import (DeckingQuote,
                                      DeckingQuoteBase, DeckingQuoteCreate,
                                      DeckingQuoteUpdate)
from app.utils import randomFloat, randomInt


class DeckingQuoteBusiness():

    def create(self, item: DeckingQuoteCreate) -> str | None:
        estimated_item = self.estimate(item)

        if (inserted_id := services.decking_quote.create(estimated_item)):
            return inserted_id

        return None

    def read_all(self) -> List[DeckingQuote]:
        deck_quotes: List[DeckingQuote] = services.decking_quote.read_all()

        return deck_quotes

    def read(self, id: str) -> DeckingQuote | None:
        if (decking_quote := services.decking_quote.read(id)) is not None:
            return decking_quote

        return None

    def update(self, id: str, item: DeckingQuoteUpdate) -> bool | None:
        processed_deck_quote_dict: dict = self.estimate(item).model_dump()
        processed_deck_quote = DeckingQuoteUpdate(**processed_deck_quote_dict)

        if (services.decking_quote.update(id, processed_deck_quote)):
            return True

        return None

    def delete(self, id: str):
        if (services.decking_quote.delete(id)):
            return True

        return None

    def estimate(self, decking_quote: DeckingQuoteBase) -> DeckingQuoteBase:

        decking_quote.updated_at = datetime.now()
        decking_quote.created_at = decking_quote.updated_at if decking_quote.created_at is None else decking_quote.created_at

        selected_spec_index: int = 0
        obj: dict = {}
        catalogs: List[Catalog] = []

        # Boards breakdown
        selected_spec_index = getattr(decking_quote, 'board_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_board.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.board_specs = CatalogSpecs(**obj)

        # Railing breakdown
        selected_spec_index = getattr(decking_quote, 'railing_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_railing.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.railing_specs = CatalogSpecs(**obj)

        # PT Frame
        selected_spec_index = getattr(decking_quote, 'pressure_treated_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_pt_frame.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.pressure_treated_specs = CatalogSpecs(**obj)

        # Structural
        selected_spec_index = getattr(decking_quote, 'structural_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_structural.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.structural_specs = CatalogSpecs(**obj)

        # Finishing
        selected_spec_index = getattr(decking_quote, 'finishing_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_finishing.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.finishing_specs = CatalogSpecs(**obj)

        # Rain Scape
        selected_spec_index = getattr(decking_quote, 'rain_scape_specs.selected_spec_index', 0)
        catalogs = business.decking_catalog_rain_scape.read_all()
        obj = {
            'selected_spec_index': selected_spec_index,
            'catalogs_spec': self.process_catalog_specs(catalogs)
        }
        decking_quote.rain_scape_specs = CatalogSpecs(**obj)

        decking_quote.profit = randomFloat(3000, 5000)
        decking_quote.value = randomFloat(15000, 30000)

        return decking_quote

    def process_catalog_specs(self, catalogs: List[Catalog]) -> List[CatalogItemSpec]:
        # catalogs_spec
        catalog_specs: List[CatalogItemSpec] = []
        for catalog in catalogs:
            catalog_spec_name: str | None = catalog.name

            # catalog_materials_spec
            catalog_materials_spec: List[CatalogMaterialSpec] = []
            for catalog_material in catalog.materials if catalog.materials is not None else []:
                qty: float | None = 0.0
                price_snapshot: float | None = 0.0
                desc: str | None = ''

                if material := business.material.read(catalog_material.id):
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


decking_quote = DeckingQuoteBusiness()
