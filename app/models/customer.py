from typing import List
from pydantic import EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber

from app.models.base import AppBaseModel


class Customer(AppBaseModel):
    id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    home_address: str | None = None
    phones: List[str] | None = None
    emails: List[EmailStr] | None = None
    notes: str | None = None
    job_address: List[str] | None = None


class CustomerEntity(AppBaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    home_address: str = Field(max_length=100)
    phones: List[str] | None = Field(max_length=10)
    emails: List[EmailStr] | None = Field(max_length=10)
    notes: str | None = Field(max_length=500)
    job_address: List[str] | None = Field(max_length=10)


class CreateCustomerDTO(CustomerEntity):
    first_name: str
    last_name: str
    home_address: str
