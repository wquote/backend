
from typing import List

from bson import ObjectId

from app.database import db
from app.models.customer import CustomerModel, CustomerCreateModel, CustomerUpdateModel


COLLECTION = 'customers'
collection = db[COLLECTION]


class CustomerService():
    def create(self, item: CustomerModel) -> str | None:
        if (result := collection.insert_one(item.dict())):
            if item_dict := collection.find_one({'_id': result.inserted_id}):
                item_inserted: CustomerModel = CustomerModel(**item_dict)

                return item_inserted.id

        return None

    def read_all(self) -> List[CustomerModel]:
        items_dict: List[dict] = list(collection.find())
        items: List[CustomerModel] = []

        for d in items_dict:
            items.append(CustomerModel(**d))

        return items

    def read(self, id: str) -> CustomerModel | None:
        if (item_dict := collection.find_one({'id': id})) is not None:
            item: CustomerModel = CustomerModel(**item_dict)

            return item

        return None

    def update(self, id: str, item: CustomerUpdateModel) -> bool | None:
        if (collection.find_one_and_update({'id': id}, {'$set': item.dict()})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


customer = CustomerService()
