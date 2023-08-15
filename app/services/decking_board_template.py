
from app.models.decking_board_template import DeckingBoardTemplate
from app.services.base import BaseService


collection = 'decking_board_templates'

decking_board_template = BaseService(collection, DeckingBoardTemplate)
