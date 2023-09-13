from app.models.customer import Customer
from app.repositories.base import BaseService


class CustomerService(BaseService):
    pass


customer: CustomerService = CustomerService('customers', Customer)
