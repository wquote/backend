from app.models.customer import Customer
from app.services.base import BaseService


class CustomerService(BaseService):
    pass


customer: CustomerService = CustomerService('customers', Customer)
