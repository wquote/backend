
from typing import List
from pydantic import BaseModel, EmailStr, Field

from app.utils import generate_uuid4


class CustomerJobAddress(BaseModel):
    id: str
    address: str
    alias: str


class CustomerModel(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    address: str | None
    phone: str | None
    email: EmailStr | None
    job_address: List[CustomerJobAddress] | None


class CustomerCreateModel(CustomerModel):
    id: str = Field(default_factory=lambda: generate_uuid4())


class CustomerUpdateModel(BaseModel):
    name: str | None
    address: str | None
    phone: str | None
    email: EmailStr | None
    job_address: List[CustomerJobAddress] | None
