from typing import List

from app import services
from app.models.deck_board_template import (DeckBoardTemplateModel,
                                            DeckBoardTemplateUpdateModel)


class DeckBoardMaterialsTemplateBusiness():
    def create(self, item: DeckBoardTemplateModel) -> str | None:
        item_id: str | None = services.deck_board_template.create(item)

        return item_id if item_id is not None else None

    def read_all(self) -> List[DeckBoardTemplateModel]:
        items: List[DeckBoardTemplateModel] = services.deck_board_template.read_all()

        return items

    def read(self, id: str) -> DeckBoardTemplateModel | None:
        item: DeckBoardTemplateModel | None = services.deck_board_template.read(id)

        return item if item is not None else None

    def update(self, id: str, item: DeckBoardTemplateUpdateModel) -> bool | None:
        if (services.deck_board_template.update(id, item)):
            return True

        return None

    def delete(self, id: str):
        if (services.deck_board_template.delete(id)):
            return True

        return None


deck_board_template = DeckBoardMaterialsTemplateBusiness()
