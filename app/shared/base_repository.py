
from typing import Any, List

from bson import ObjectId
from fastapi import HTTPException
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from app.database import db
from app.utils import decodeObjId


def raise_error(e: Exception) -> str:
    print(f'Error: {e}')
    raise HTTPException(status_code=500, detail='Error: ' + str(e))


def raise_not_found(item_name: str) -> str:
    raise HTTPException(status_code=404, detail=item_name + ' not found.')


def raise_not_created(item_name: str) -> str:
    raise HTTPException(status_code=422, detail=item_name + ' not created.')


class BaseRepository():
    """
    BaseRepository class provides basic CRUD operations for a MongoDB collection.

    Args:
        collection (str): The name of the MongoDB collection.
        dto: The dto class representing the data model.

    Attributes:
        collection: The MongoDB collection object.
        dto: The dto class representing the data model.

    """

    def __init__(self, collection: str, dto) -> None:
        self.collection = db[collection]
        self.dto = dto

    def create(self, item) -> str | None:
        """
        Create a new item in the collection.

        Args:
            item: The item to be created.

        Returns:
            str | None: The inserted item's ID if successful, None otherwise.

        Raises:
            Exception: If an error occurs during the operation.

        """
        try:
            item_dict: dict = item.model_dump()
            result: InsertOneResult = self.collection.insert_one(item_dict)
            if result.inserted_id:
                return str(result.inserted_id)

        except Exception as e:
            raise_error(e)

        return None

    def read_all(self) -> List:
        """
        Retrieve all items from the collection.

        Returns:
            List: A list of items retrieved from the collection.

        Raises:
            Exception: If an error occurs during the operation.

        """
        try:
            items_list: List[dict] = list(self.collection.find())
            items = [self.dto(**decodeObjId(i)) for i in items_list]

        except Exception as e:
            raise_error(e)

        return items

    def read(self, id: str) -> Any | None:
        """
        Retrieve an item from the collection by its ID.

        Args:
            id (str): The ID of the item to retrieve.

        Returns:
            Any | None: The retrieved item if found, None otherwise.

        Raises:
            Exception: If an error occurs during the operation.
            NotFoundError: If the item is not found in the collection.

        """
        try:
            if item_dict := self.collection.find_one({'_id': ObjectId(id)}):
                item = self.dto(**decodeObjId(item_dict))
                return item
            else:
                raise_not_found(self.dto.__name__)

        except Exception as e:
            raise_error(e)

        return None

    def update(self, id: str, item) -> bool:
        """
        Update an item in the collection by its ID.

        Args:
            id (str): The ID of the item to update.
            item: The updated item.

        Returns:
            bool: True if the item is updated successfully, False otherwise.

        Raises:
            Exception: If an error occurs during the operation.
            NotFoundError: If the item is not found in the collection.

        """
        try:
            item_dict: dict = item.model_dump()
            result: UpdateResult = self.collection.update_one({'_id': ObjectId(id)}, {'$set': item_dict})
            if (result.matched_count == 1):
                return True
            else:
                raise_not_found(self.dto.__name__)

        except Exception as e:
            raise_error(e)

        return False

    def delete(self, id: str) -> bool:
        """
        Delete an item from the collection by its ID.

        Args:
            id (str): The ID of the item to delete.

        Returns:
            bool: True if the item is deleted successfully, False otherwise.

        Raises:
            Exception: If an error occurs during the operation.
            NotFoundError: If the item is not found in the collection.

        """
        try:
            result: DeleteResult = self.collection.delete_one({'_id': ObjectId(id)})
            if (result.deleted_count == 1):
                return True
            else:
                raise_not_found(self.dto.__name__)

        except Exception as e:
            raise_error(e)

        return False
