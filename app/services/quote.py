
from typing import List

from bson import ObjectId

from app.database import db
from app.models.quote import QuoteModel


collection = db['quotes']


class QuoteService():
    def read_all(self) -> List[QuoteModel]:
        items_dict: List[dict] = list(collection.find())
        items: List[QuoteModel] = []

        for i in items_dict:
            items.append(QuoteModel(**i))

        return items

    def read(self, id: str) -> QuoteModel | None:
        if (item_dict := collection.find_one({'id': id})) is not None:
            item: QuoteModel = QuoteModel(**item_dict)

            return item

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


quote = QuoteService()
