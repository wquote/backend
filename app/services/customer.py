
from app import repositories
from app.services.base import BaseBusiness


class CustomerBusiness(BaseBusiness):
    pass


customer = CustomerBusiness(repositories.customer)
