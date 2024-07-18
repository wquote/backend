from app.shared.base_repository import BaseRepository, raise_error, raise_not_found
from app.utils import decodeObjId

from .user_model import User, UserInDB

collection = "users"
entity = User


class UserRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)

    def read_by_username(self, username: str) -> UserInDB | None:
        try:
            if item_dict := self.collection.find_one({"username": username}):
                item = UserInDB(**decodeObjId(item_dict))
                return item
            else:
                raise_not_found(self.entity.__name__)

        except Exception as e:
            raise_error(e)

        return None


user_repository: UserRepository = UserRepository(collection, entity)
