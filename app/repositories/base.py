
from typing import Any, List

from bson import ObjectId
from fastapi import HTTPException
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from app.database import db
from app.utils import decodeObjId


def raise_error(e: Exception) -> str:
    raise HTTPException(status_code=500, detail='Validation Error: ' + str(e))


def raise_not_found(item_name: str) -> str:
    raise HTTPException(status_code=404, detail=item_name + ' not found.')


class BaseRepository():

    def __init__(self, collection: str, entity) -> None:
        self.collection = db[collection]
        self.entity = entity

    def create(self, item) -> str | None:
        try:
            item_dict: dict = item.model_dump()
            result: InsertOneResult = self.collection.insert_one(item_dict)
            if result.inserted_id:
                return str(result.inserted_id)

        except Exception as e:
            raise_error(e)

        return None

    def read_all(self) -> List:
        try:
            items_list: List[dict] = list(self.collection.find())
            items = [self.entity(**decodeObjId(i)) for i in items_list]

        except Exception as e:
            raise_error(e)

        return items

    def read(self, id: str) -> Any | None:
        try:
            if item_dict := self.collection.find_one({'_id': ObjectId(id)}):
                item = self.entity(**decodeObjId(item_dict))
                return item

        except Exception as e:
            raise_error(e)

        return None

    def update(self, id: str, item) -> bool:
        try:
            item_dict: dict = item.model_dump()
            result: UpdateResult = self.collection.update_one({'_id': ObjectId(id)}, {'$set': item_dict})
            if (result.matched_count == 1):
                return True

        except Exception as e:
            raise_error(e)

        return False

    def delete(self, id: str) -> bool:
        try:
            result: DeleteResult = self.collection.delete_one({'_id': ObjectId(id)})
            if (result.deleted_count == 1):
                return True

        except Exception as e:
            raise_error(e)

        return False
