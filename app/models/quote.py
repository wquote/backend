
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class QuoteModel(BaseModel):
    id: str
    id_customer: str
    type: str
    date: datetime | None
    profit: float | None
    total_cost: float | None


class QuoteUpdateModel(BaseModel):
    id_customer: str
    type: str
    date: datetime | None
    profit: float | None
    total_cost: float | None


class QuoteDTO(BaseModel):
    id: str
    name_customer: str
    type: str
    date: datetime
    profit: float
    total_cost: float
