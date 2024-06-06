from app.shared.base_service import BaseService

from .dmo_railing_repository import dmo_railing_repository


class DeckingMaterialOrderRaillingService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_railing_service = DeckingMaterialOrderRaillingService(dmo_railing_repository)
