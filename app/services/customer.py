
from typing import List

from fastapi.encoders import jsonable_encoder

from app.database import db
from app.models.customer import Customer, CustomerCreate, CustomerInDB, CustomerUpdate

collection = db['customers']


class CustomerService():
    def create(self, item: CustomerCreate) -> str | None:
        # '_id' creation with PyObjectId class
        item_indb: CustomerInDB = CustomerInDB(**item.model_dump())
        item_indb_dict: dict = jsonable_encoder(item_indb)

        if (result := collection.insert_one(item_indb_dict)):
            return result.inserted_id

        return None

    def read_all(self) -> List[Customer]:
        items_dict: List[dict] = list(collection.find())
        items: List[Customer] = []

        for d in items_dict:
            items.append(Customer(**d))

        return items

    def read(self, id: str) -> Customer | None:
        if (item_dict := collection.find_one({'_id': id})):
            item: Customer = Customer(**item_dict)

            return item

        return None

    def update(self, id: str, item: CustomerUpdate) -> bool | None:
        item_dict: dict = jsonable_encoder(item)
        if (collection.find_one_and_update({'_id': id}, {'$set': item_dict})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'_id': id})) is not None:
            return True

        return None


customer = CustomerService()
