from typing import Any, Dict, List

from fastapi import HTTPException, status


class BaseController:
    """
    Base controller class for handling CRUD operations.

    Args:
        service: The service object responsible for interacting with the data layer.
        item_name (str): The name of the item being handled by the controller.

    Attributes:
        service: The service object responsible for interacting with the data layer.
        NOT_FOUND_MSG (str): The error message to be raised when an item is not found.
        NOT_CREATED_MSG (str): The error message to be raised when an item is not created.
    """

    def __init__(self, service, item_name: str):
        self.service = service
        self.NOT_FOUND_MSG = item_name + " not found."
        self.NOT_CREATED_MSG = item_name + " not created."

    def create(self, body) -> Dict:
        """
        Create a new item.

        Args:
            body: The data for creating the item.

        Returns:
            dict: The created item.

        Raises:
            HTTPException: If the item could not be created.
        """
        inserted_id: str | None = self.service.create(body)

        if inserted_id is not None:
            return {"id": inserted_id}

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=self.NOT_CREATED_MSG
        )

    def read_all(self) -> List:
        """
        Read all items.

        Returns:
            list: A list of all items.

        Raises:
            HTTPException: If no items are found.
        """
        items: List = self.service.read_all()
        if items:
            return items

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def read(self, id: str) -> Any:
        """
        Read an item by its ID.

        Args:
            id (str): The ID of the item to read.

        Returns:
            Any: The item with the specified ID, or None if not found.

        Raises:
            HTTPException: If the item with the specified ID is not found.
        """
        if item := self.service.read(id):
            return item

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def update(self, id: str, body) -> bool:
        """
        Update an item by its ID.

        Args:
            id (str): The ID of the item to update.
            body: The updated data for the item.

        Returns:
            bool: True if the item was successfully updated, False otherwise.

        Raises:
            HTTPException: If the item with the specified ID is not found.
        """
        if self.service.update(id, body):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)

    def delete(self, id: str) -> bool:
        """
        Delete an item by its ID.

        Args:
            id (str): The ID of the item to delete.

        Returns:
            bool: True if the item was successfully deleted, False otherwise.

        Raises:
            HTTPException: If the item with the specified ID is not found.
        """
        if self.service.delete(id):
            return True

        raise HTTPException(status_code=404, detail=self.NOT_FOUND_MSG)
