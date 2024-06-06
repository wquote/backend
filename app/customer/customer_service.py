from app.shared.base_service import BaseService

from .customer_repository import customer_repository


class CustomerService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


customer_service: CustomerService = CustomerService(customer_repository)
