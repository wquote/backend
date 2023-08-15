from datetime import datetime
from typing import List

from app import business, services
from app.models.decking_board_template import DeckingBoardTemplate
from app.models.decking_quote import (DeckingBoardSpec,
                                      DeckingBoardSpecMaterial, DeckingQuote,
                                      DeckingQuoteCreate, DeckingQuoteUpdate)
from app.utils import randomFloat, randomInt


class DeckingQuoteBusiness():

    def create(self, item: DeckingQuoteCreate) -> str | None:
        processed_item = self.process_quote(item)

        if (inserted_id := services.decking_quote.create(processed_item)):
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
        processed_deck_quote_dict: dict = self.process_quote(item).model_dump()
        processed_deck_quote = DeckingQuoteUpdate(**processed_deck_quote_dict)

        if (services.decking_quote.update(id, processed_deck_quote)):
            return True

        return None

    def delete(self, id: str):
        if (services.decking_quote.delete(id)):
            return True

        return None

    def process_quote(self, decking_quote: DeckingQuoteCreate | DeckingQuoteUpdate
                      ) -> DeckingQuoteCreate | DeckingQuoteUpdate:

        decking_quote.date = datetime.now()

        decking_quote.decking_board_specs = self.process_board_specs()

        decking_quote.profit = randomFloat(3000, 5000)
        decking_quote.value = randomFloat(15000, 30000)

        return decking_quote

    def process_board_specs(self) -> List[DeckingBoardSpec]:
        templates: List[DeckingBoardTemplate] = business.decking_board_template.read_all()

        # decking_board_specs
        board_specs: List[DeckingBoardSpec] = []
        for template in templates:
            template_name: str | None = template.name

            # decking_board_spec_materials
            board_spec_materials: List[DeckingBoardSpecMaterial] = []
            if template.materials:
                for m in template.materials:
                    if m.is_default:
                        material_id: str = m.id
                        qty: float = randomInt(5, 15)
                        price_snapshot: float | None = 0.0
                        desc: str | None = ''

                        if material := business.material.read(material_id):
                            price_snapshot = material.price
                            desc = material.desc

                        obj: dict = {
                            "desc_snapshot": desc,
                            "price_snapshot": price_snapshot,
                            "qty": qty,
                        }

                        board_spec_materials.append(DeckingBoardSpecMaterial(**obj))

            amount_sum: float = sum(material.price_snapshot * float(material.qty) for material in board_spec_materials)
            tax: float = 0.0625 * amount_sum
            cost: float = amount_sum + tax

            obj = dict(
                name=template_name,
                materials=board_spec_materials,
                tax=tax,
                cost=cost
            )

            board_spec = DeckingBoardSpec(**obj)
            board_specs.append(board_spec)

        return board_specs


decking_quote = DeckingQuoteBusiness()
