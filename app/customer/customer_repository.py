from app.shared.base_repository import BaseRepository

from .customer_model import Customer

collection = "customers"
entity = Customer


class CustomerRepository(BaseRepository):
    def __init__(self, collection: str, entity):
        super().__init__(collection, entity)


customer_repository: CustomerRepository = CustomerRepository(collection, entity)
