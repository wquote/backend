from app.shared.base_service import BaseService

from .dmo_board_repository import dmo_board_repository


class DeckingMaterialOrderBoardService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


dmo_board_service = DeckingMaterialOrderBoardService(dmo_board_repository)
