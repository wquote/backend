
from datetime import datetime
from typing import Annotated, List
from bson import ObjectId

from pydantic import Field

from app.models.base import AppBaseModel, PyObjectId


class QuoteBase(AppBaseModel):
    id_customer: str | None = None
    job_address: str | None = None
    type: str | None = None
    date: datetime | None = None
    profit: float | None = None
    value: float | None = None
    notes: str | None = None


class Quote(QuoteBase):
    id: str = Field(alias='_id')


class QuoteCreate(QuoteBase):
    id_customer: str
    job_address: str
    type: str


class QuoteUpdate(QuoteBase):
    pass


class QuoteInDB(QuoteBase):
    id: Annotated[ObjectId, PyObjectId] = Field(default_factory=ObjectId, alias='_id')

    class Config:
        json_encoders = {ObjectId: str}
