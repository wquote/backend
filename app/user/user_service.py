from app.shared.base_service import BaseService
from app.user.user_model import UserInDB

from .user_repository import user_repository


class UserService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)

    def read_by_username(self, username: str) -> UserInDB | None:
        return self.repository.read_by_username(username)


user_service: UserService = UserService(user_repository)
