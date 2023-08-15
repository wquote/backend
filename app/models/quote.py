
from datetime import datetime
from enum import Enum

from app.models.base import AppBaseModel


class JobType(str, Enum):
    decking = 'DECKING'
    roofing = 'ROOFING'
    siding = 'SIDING'


class QuoteBase(AppBaseModel):
    customer_id: str | None = None
    job_address: str | None = None
    type: JobType | None = None
    date: datetime | None = None
    profit: float | None = None
    value: float | None = None
    notes: str | None = None


class Quote(QuoteBase):
    id: str


class QuoteCreate(QuoteBase):
    customer_id: str
    job_address: str
    type: JobType


class QuoteUpdate(QuoteBase):
    pass
