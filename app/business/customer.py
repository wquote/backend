
from app import services
from app.business.base import BaseBusiness


class CustomerBusiness(BaseBusiness):
    pass


customer = CustomerBusiness(services.customer)
