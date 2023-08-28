from typing import List

from app import services
from app.models.decking_board_catalog import (DeckingBoardCatalog,
                                              DeckingBoardCatalogCreate,
                                              DeckingBoardCatalogUpdate)


class DeckBoardMaterialsCatalogBusiness():
    def create(self, item: DeckingBoardCatalogCreate) -> str | None:
        item_id: str | None = services.decking_board_catalog.create(item)

        return item_id if item_id is not None else None

    def read_all(self) -> List[DeckingBoardCatalog]:
        items: List[DeckingBoardCatalog] = services.decking_board_catalog.read_all()

        return items

    def read(self, id: str) -> DeckingBoardCatalog | None:
        item: DeckingBoardCatalog | None = services.decking_board_catalog.read(id)

        return item if item is not None else None

    def update(self, id: str, item: DeckingBoardCatalogUpdate) -> bool | None:
        if (services.decking_board_catalog.update(id, item)):
            return True

        return None

    def delete(self, id: str):
        if (services.decking_board_catalog.delete(id)):
            return True

        return None


decking_board_catalog = DeckBoardMaterialsCatalogBusiness()
