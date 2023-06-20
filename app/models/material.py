
from pydantic import BaseModel, Field

from app.utils import generate_uuid4


class MaterialModel(BaseModel):
    id: str
    desc: str
    price: float = Field(ge=0)
    supplier: str | None


class MaterialCreateModel(MaterialModel):
    id: str = Field(default_factory=lambda: generate_uuid4())


class MaterialUpdateModel(BaseModel):
    desc: str | None
    price: float | None = Field(ge=0)
    supplier: str | None
