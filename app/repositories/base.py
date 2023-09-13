
from typing import Any, List, Type, TypeVar

from bson import ObjectId
from bson.errors import InvalidId

from app.database import db
from app.models.base import AppBaseModel
from app.utils import decodeObjId


R = TypeVar('R', bound=AppBaseModel)  # read


class BaseService():

    def __init__(self, collection: str, read_model: Type[R] | None = None) -> None:
        self.collection = db[collection]
        self.read_model = read_model

    def create(self, item) -> str | None:
        item_dict: dict = item.model_dump()

        if (result := self.collection.insert_one(item_dict)):
            return str(result.inserted_id)

        return None

    def read_all(self) -> List:
        items_list: List[dict] = list(self.collection.find())
        items: List = [self.read_model(**decodeObjId(i)) for i in items_list if self.read_model]

        return items

    def read(self, id: str) -> Any | None:
        try:
            if (item_dict := self.collection.find_one({'_id': ObjectId(id)})):
                item = self.read_model(**decodeObjId(item_dict)) if self.read_model else None
                return item

            return None

        except InvalidId:
            return None

    def update(self, id: str, item) -> bool | None:
        item_dict: dict = item.model_dump()
        if (self.collection.update_one({'_id': ObjectId(id)}, {'$set': item_dict})):
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (self.collection.delete_one({'_id': ObjectId(id)})):
            return True

        return None
