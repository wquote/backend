from app.shared.base_service import BaseService

from .dmo_finishing_repository import dmo_finishing_repository

repository = dmo_finishing_repository


class DeckingMaterialOrderFinishingService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_finishing_service = DeckingMaterialOrderFinishingService(repository)
