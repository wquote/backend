from app.models.customer import Customer, CustomerCreate, CustomerUpdate
from app.services.base import BaseService

customer = BaseService('customers', Customer)
