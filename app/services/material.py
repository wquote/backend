
from app import repositories
from app.services.base import BaseService


class MaterialService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


material = MaterialService(repositories.material)
