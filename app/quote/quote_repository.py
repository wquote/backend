from typing import List

from app.database import db
from app.quote.quote_models import Quote
from app.shared.base_repository import BaseRepository
from app.utils import decodeObjId

collection = "quotes"
entity = Quote
db_collection = db[collection]


class QuoteRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)

    def read_by_customer(self, customer_id: str) -> List[Quote]:
        items_list: List[dict] = list(db_collection.find({"customer_id": customer_id}))
        items: List = [Quote(**decodeObjId(i)) for i in items_list]

        return items


quote_repository: QuoteRepository = QuoteRepository(collection, entity)
