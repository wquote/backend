from datetime import datetime
from enum import Enum

from app.shared.base_model import AppBaseModel


class JobType(str, Enum):
    decking = "DECKING"
    roofing = "ROOFING"
    siding = "SIDING"


class QuoteState(str, Enum):
    opened = "OPENED"
    closed = "CLOSED"


class QuoteBase(AppBaseModel):
    customer_id: str | None = None
    job_address: str | None = None
    type: JobType | None = None
    notes: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    closed_at: datetime | None = None
    state: QuoteState | None = None
    profit: float | None = None
    profit_percent: float | None = None
    value: float | None = None


class Quote(QuoteBase):
    id: str


class QuoteCreate(QuoteBase):
    customer_id: str = ""
    job_address: str = ""


class QuoteUpdate(QuoteBase):
    pass
