
from typing import List

from app.database import db
from app.models.deck_board_template import DeckBoardTemplateModel, DeckBoardTemplateUpdateModel


collection = db['deck_board_templates']


class DeckBoardMaterialsTemplateService():
    def create(self, deckboard_type: DeckBoardTemplateModel) -> str | None:
        if (result := collection.insert_one(deckboard_type.dict())):
            if item_dict := collection.find_one({'_id': result.inserted_id}):
                item: DeckBoardTemplateModel = DeckBoardTemplateModel(**item_dict)

                return item.id

        return None

    def read_all(self) -> List[DeckBoardTemplateModel]:
        deckboard_types_dict: List[dict] = list(collection.find())
        deckboard_types: List[DeckBoardTemplateModel] = []

        for d in deckboard_types_dict:
            deckboard_types.append(DeckBoardTemplateModel(**d))

        return deckboard_types

    def read(self, id: str) -> DeckBoardTemplateModel | None:
        if (deckboard_type_dict := collection.find_one({'id': id})) is not None:
            deckboard_type: DeckBoardTemplateModel = DeckBoardTemplateModel(**deckboard_type_dict)

            return deckboard_type

        return None

    def update(self, id: str, deckboard_type: DeckBoardTemplateUpdateModel) -> bool | None:
        if (collection.find_one_and_update({'id': id}, {'$set': deckboard_type.dict()})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


deck_board_template = DeckBoardMaterialsTemplateService()
