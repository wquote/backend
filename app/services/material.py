
from app import repositories
from app.services.base import BaseBusiness


class MaterialBusiness(BaseBusiness):
    pass


material = MaterialBusiness(repositories.material)
