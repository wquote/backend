
from app import repositories
from app.models.customer import Customer
from app.models.material import Material
from app.services.base import BaseService


class CustomerService(BaseService):
    def __init__(self, repository, read_model):
        super().__init__(repository, read_model)


customer = CustomerService(repositories.customer, Material)
