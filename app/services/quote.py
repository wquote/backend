
from typing import List

from bson import ObjectId

from app.database import db
from app.models.quote import Quote


collection = db['quotes']


class QuoteService():
    def read(self, id: str) -> Quote | None:
        if (item_dict := collection.find_one({'_id': id})) is not None:
            item: Quote = Quote(**item_dict)

            return item

        return None

    def read_all(self) -> List[Quote]:
        items_dict: List[dict] = list(collection.find())
        items: List[Quote] = []

        for i in items_dict:
            items.append(Quote(**i))

        return items

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items_dict: List[dict] = list(collection.find({'customer_id': customer_id}))
        items: List[Quote] = []

        for i in items_dict:
            items.append(Quote(**i))

        return items

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'_id': id})) is not None:
            return True

        return None


quote = QuoteService()
