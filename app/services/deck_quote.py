
from typing import List

from fastapi.encoders import jsonable_encoder

from app.database import db
from app.models.deck_quote import DeckQuote, DeckQuoteCreate, DeckQuoteUpdate, DeckQuoteInDB


collection = db['quotes']


class DeckQuoteService():
    def create(self, item: DeckQuoteCreate) -> str | None:
        # '_id' creation with PyObjectId class
        item_indb: DeckQuoteInDB = DeckQuoteInDB(**item.model_dump())
        item_indb_dict: dict = jsonable_encoder(item_indb)

        if (result := collection.insert_one(item_indb_dict)):
            return result.inserted_id

        return None

    def read_all(self) -> List[DeckQuote]:
        decks_dict: List[dict] = list(collection.find())
        decks: List[DeckQuote] = []

        for d in decks_dict:
            decks.append(DeckQuote(**d))

        return decks

    def read(self, id: str) -> DeckQuote | None:
        if (deck_dict := collection.find_one({'id': id})) is not None:
            item: DeckQuote = DeckQuote(**deck_dict)

            return item

        return None

    def update(self, id: str, item: DeckQuoteUpdate) -> bool | None:
        if (collection.find_one_and_update({'id': id}, {'$set': item.dict()})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


deck_quote = DeckQuoteService()
