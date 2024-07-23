from typing import List

from pydantic import EmailStr, Field

from app.shared.base_model import AppBaseModel

# from pydantic_extra_types.phone_numbers import PhoneNumber


class CustomerBase(AppBaseModel):
    first_name: str | None = None
    last_name: str | None = None
    home_address: str | None = None
    phones: List[str] | None = []
    emails: List[EmailStr] | None = []
    notes: str | None = None
    job_address: List[str] | None = []


class Customer(CustomerBase):
    id: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass
