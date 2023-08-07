from typing import Annotated, List
import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from bson import ObjectId

from app.models.base import AppBaseModel, PyObjectId


class CustomerBase(AppBaseModel):
    first_name: str | None = None
    last_name: str | None = None
    home_address: str | None = None
    phones: List[str] | None = None
    emails: List[EmailStr] | None = None
    notes: str | None = None
    job_address: List[str] | None = None


class Customer(CustomerBase):
    id: str = Field(alias='_id')


class CustomerCreate(CustomerBase):
    first_name: str
    last_name: str


class CustomerUpdate(CustomerBase):
    pass


class CustomerInDB(CustomerBase):
    id: Annotated[ObjectId, PyObjectId] = Field(default_factory=ObjectId, alias='_id')

    class Config:
        json_encoders = {ObjectId: str}
