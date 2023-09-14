
from typing import List

from bson import ObjectId

from app.database import db
from app.models.quote import Quote
from app.repositories.base import BaseRepository
from app.utils import decodeObjId

collection = db['quotes']


class QuoteService(BaseRepository):

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items_list: List[dict] = list(collection.find({'customer_id': customer_id}))
        items: List = [Quote(**decodeObjId(i)) for i in items_list]

        return items


quote = QuoteService('quotes', Quote)
