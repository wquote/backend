from app.models.customer import Customer
from app.repositories.base import BaseRepository

collection: str = 'customers'
entity = Customer

customer = BaseRepository(collection, entity)
