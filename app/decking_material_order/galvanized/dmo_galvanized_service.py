from app.shared.base_service import BaseService

from .dmo_galvanized_repository import dmo_galvanized_repository


class DeckingMaterialOrderGalvanizedService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_galvanized_service = DeckingMaterialOrderGalvanizedService(dmo_galvanized_repository)