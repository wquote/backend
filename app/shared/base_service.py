from typing import Any, List


class BaseService:
    """
    Base service class for performing CRUD operations on items.
    """

    def __init__(self, repository) -> None:
        """
        Initialize the BaseService with a repository.

        Args:
            repository: The repository object used for data access.
        """
        self.repository = repository

    def create(self, item) -> str | None:
        """
        Create a new item.

        Args:
            item: The item to be created.

        Returns:
            The ID of the created item, or None if creation fails.
        """
        item_id: str | None = self.repository.create(item)
        return item_id if item_id else None

    def read_all(self) -> List:
        """
        Read all items.

        Returns:
            A list of all items.
        """
        return self.repository.read_all()

    def read(self, id: str) -> Any:
        """
        Read an item by its ID.

        Args:
            id: The ID of the item to be read.

        Returns:
            The item with the specified ID, or None if not found.
        """
        item = self.repository.read(id)
        return item if item else None

    def update(self, id: str, item) -> bool:
        """
        Update an item.

        Args:
            id: The ID of the item to be updated.
            item: The updated item.

        Returns:
            True if the update is successful, False otherwise.
        """
        return True if self.repository.update(id, item) else False

    def delete(self, id: str) -> bool:
        """
        Delete an item.

        Args:
            id: The ID of the item to be deleted.

        Returns:
            True if the deletion is successful, False otherwise.
        """
        return True if self.repository.delete(id) else False
