
from app import repositories
from app.services.base import BaseService


class CustomerService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)


customer = CustomerService(repositories.customer)
