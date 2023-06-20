
from typing import List

from app.database import db
from app.models.deck_quote import DeckQuoteModel, DeckQuoteUpdateModel


collection = db['quotes']


class DeckQuoteService():
    def create(self, deck_quote: DeckQuoteModel) -> str | None:
        if (result := collection.insert_one(deck_quote.dict())) is not None:
            return str(result.inserted_id)

        return None

    def read_all(self) -> List[DeckQuoteModel]:
        decks_dict: List[dict] = list(collection.find())
        decks: List[DeckQuoteModel] = []

        for d in decks_dict:
            decks.append(DeckQuoteModel(**d))

        return decks

    def read(self, id: str) -> DeckQuoteModel | None:
        if (deck_dict := collection.find_one({'id': id})) is not None:
            item: DeckQuoteModel = DeckQuoteModel(**deck_dict)

            return item

        return None

    def update(self, id: str, item: DeckQuoteUpdateModel) -> bool | None:
        if (collection.find_one_and_update({'id': id}, {'$set': item.dict()})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


deck_quote = DeckQuoteService()
