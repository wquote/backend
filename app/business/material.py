
from app import services
from app.business.base import BaseBusiness


class MaterialBusiness(BaseBusiness):
    pass


material = MaterialBusiness(services.material)
