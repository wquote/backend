from datetime import datetime
from typing import List

from app import business, services
from app.models.deck_quote import (DeckBoardSpecification, DeckBoardSpecMaterialModel,
                                   DeckQuoteModel, DeckQuoteUpdateModel, DeckModel)
from app.models.deck_board_template import DeckBoardTemplateModel


class DeckQuoteBusiness():

    def create(self, deck_quote: DeckQuoteModel) -> str | None:
        processed_deck_quote_dict: dict = self.process_quote(deck_quote).dict()
        processed_deck_quote = DeckQuoteModel(**processed_deck_quote_dict)

        if (inserted_id := services.deck_quote.create(processed_deck_quote)) is not None:
            return inserted_id

        return None

    def read_all(self) -> List[DeckQuoteModel]:
        deck_quotes: List[DeckQuoteModel] = services.deck_quote.read_all()

        return deck_quotes

    def read(self, id: str) -> DeckQuoteModel | None:
        if (deck_quote := services.deck_quote.read(id)) is not None:
            return deck_quote

        return None

    def update(self, id: str, deck_quote: DeckQuoteUpdateModel) -> bool | None:
        processed_deck_quote_dict: dict = self.process_quote(deck_quote).dict()
        processed_deck_quote = DeckQuoteUpdateModel(**processed_deck_quote_dict)

        if (services.deck_quote.update(id, processed_deck_quote)):
            return True

        return None

    def delete(self, id: str):
        if (services.deck_quote.delete(id)):
            return True

        return None

    def process_quote(self, deck_quote: DeckQuoteModel | DeckQuoteUpdateModel) -> DeckQuoteModel | DeckQuoteUpdateModel:
        if deck_quote.deck:
            deck = deck_quote.deck
            width: float = deck.main_areas[0].width
            depth: float = deck.main_areas[0].depth
            area: float = width * depth

        deck_quote.date = datetime.now()
        board_specs: List[DeckBoardSpecification] = self.process_board_specs(area)
        deck_quote.board_specs = board_specs
        deck_quote.profit = board_specs[0].cost * 1.20
        deck_quote.total_cost = board_specs[0].cost + deck_quote.profit

        return deck_quote

    def process_board_specs(self, area: float) -> List[DeckBoardSpecification]:
        deckboard_templates: List[DeckBoardTemplateModel] = business.deck_board_template.read_all()

        # board_specs
        board_specs: List[DeckBoardSpecification] = []
        for template in deckboard_templates:
            id_template: str = template.id
            name_template: str = template.name

            # materials
            board_materials: List[DeckBoardSpecMaterialModel] = []
            for m in template.materials:
                if m.is_default:
                    id_material: str = m.id
                    qty: float = area

                    price_snapshot: float = 0.0
                    desc_material: str = ''
                    if material := business.material.read(id_material):
                        price_snapshot = material.price
                        desc_material = material.desc

                    obj: dict = {
                        "id": id_material,
                        "desc": desc_material,
                        "qty": qty,
                        "price_snapshot": price_snapshot
                    }

                    board_material = DeckBoardSpecMaterialModel(**obj)
                    board_materials.append(board_material)

            amount_sum: float = sum(material.price_snapshot * material.qty for material in board_materials)
            tax: float = 0.0625 * amount_sum
            cost: float = amount_sum + tax

            obj = dict(
                id_deckboard_template=id_template,
                name=name_template,
                materials=board_materials,
                tax=tax,
                cost=cost
            )

            board_spec = DeckBoardSpecification(**obj)
            board_specs.append(board_spec)

        return board_specs


deck_quote = DeckQuoteBusiness()
