
from typing import List

from bson import ObjectId

from app.database import db
from app.models.quote import Quote
from app.services.base import BaseService
from app.utils import decodeObjId


collection = db['quotes']


class QuoteService(BaseService):

    def read_by_customer(self, id_customer: str) -> List[Quote]:
        items_list: List[dict] = list(collection.find({'id_customer': id_customer}))
        items: List = [Quote(**decodeObjId(i)) for i in items_list]

        return items


quote = QuoteService('quotes', Quote)
