
from pydantic import Field

from app.models.base import AppBaseModel


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
