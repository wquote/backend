from app.shared.base_service import BaseService

from .dmo_frame_repository import dmo_frame_repository


class DeckingMaterialOrderFrameService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_frame_service = DeckingMaterialOrderFrameService(dmo_frame_repository)