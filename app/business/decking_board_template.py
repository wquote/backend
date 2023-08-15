from typing import List

from app import services
from app.models.decking_board_template import (DeckingBoardTemplate,
                                               DeckingBoardTemplateCreate,
                                               DeckingBoardTemplateUpdate)


class DeckBoardMaterialsTemplateBusiness():
    def create(self, item: DeckingBoardTemplateCreate) -> str | None:
        item_id: str | None = services.decking_board_template.create(item)

        return item_id if item_id is not None else None

    def read_all(self) -> List[DeckingBoardTemplate]:
        items: List[DeckingBoardTemplate] = services.decking_board_template.read_all()

        return items

    def read(self, id: str) -> DeckingBoardTemplate | None:
        item: DeckingBoardTemplate | None = services.decking_board_template.read(id)

        return item if item is not None else None

    def update(self, id: str, item: DeckingBoardTemplateUpdate) -> bool | None:
        if (services.decking_board_template.update(id, item)):
            return True

        return None

    def delete(self, id: str):
        if (services.decking_board_template.delete(id)):
            return True

        return None


decking_board_template = DeckBoardMaterialsTemplateBusiness()
