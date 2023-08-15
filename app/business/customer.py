from typing import List

from app import services
from app.business.base import BaseBusiness
from app.models.customer import Customer, CustomerCreate, CustomerUpdate


class CustomerBusiness(BaseBusiness):
    pass


customer = CustomerBusiness(services.customer)
