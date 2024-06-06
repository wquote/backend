from app.shared.base_service import BaseService

from .material_repository import material_repository


class MaterialService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


material_service: MaterialService = MaterialService(material_repository)
