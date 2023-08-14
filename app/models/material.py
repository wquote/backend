
from typing import Annotated
from bson import ObjectId
from pydantic import Field

from app.models.base import AppBaseModel, PyObjectId


class MaterialBase(AppBaseModel):
    desc: str | None = None
    price: float | None = Field(ge=0)
    supplier: str | None = None


class Material(MaterialBase):
    id: str


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass


class MaterialInDB(MaterialBase):
    id: Annotated[ObjectId, PyObjectId] = Field(default_factory=ObjectId, alias='_id')

    class Config:
        json_encoders = {ObjectId: str}
