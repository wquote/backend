from pydantic import Field

from app.shared.base_model import AppBaseModel


class MaterialBase(AppBaseModel):
    reference: str | None = None
    desc: str | None = None
    price: float | None = Field(ge=0)
    supplier: str | None = None


class Material(MaterialBase):
    id: str


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass
