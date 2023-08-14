
from datetime import datetime
from enum import Enum
from typing import Annotated, List

from bson import ObjectId
from pydantic import Field

from app.models.base import AppBaseModel, PyObjectId


class JobType(str, Enum):
    decking = 'DECKING'
    roofing = 'ROOFING'
    siding = 'SIDING'


class QuoteBase(AppBaseModel):
    id_customer: str | None = None
    job_address: str | None = None
    type: JobType | None = None
    date: datetime | None = None
    profit: float | None = None
    value: float | None = None
    notes: str | None = None


class Quote(QuoteBase):
    id: str


class QuoteCreate(QuoteBase):
    id_customer: str
    job_address: str
    type: JobType


class QuoteUpdate(QuoteBase):
    pass


# class QuoteInDB(QuoteBase):
#     id: Annotated[ObjectId, PyObjectId] = Field(default_factory=ObjectId, alias='_id')

#     class Config:
#         json_encoders = {ObjectId: str}
