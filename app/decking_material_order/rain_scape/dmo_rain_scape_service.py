from app.shared.base_service import BaseService

from .dmo_rain_scape_repository import dmo_rain_scape_repository


class DeckingMaterialOrderRainScapeService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_rain_scape_service = DeckingMaterialOrderRainScapeService(dmo_rain_scape_repository)
