
from typing import List

from bson import ObjectId

from app.database import db
from app.models.material import MaterialModel, MaterialUpdateModel


COLLECTION = 'materials'
collection = db[COLLECTION]


class MaterialService():
    def create(self, material: MaterialModel) -> str | None:
        if (result := collection.insert_one(material.dict())):
            if item_dict := collection.find_one({'_id': result.inserted_id}):
                item: MaterialModel = MaterialModel(**item_dict)

                return item.id

        return None

    def read_all(self) -> List[MaterialModel]:
        materials_dict: List[dict] = list(collection.find())
        materials: List[MaterialModel] = []

        for d in materials_dict:
            materials.append(MaterialModel(**d))

        return materials

    def read(self, id: str) -> MaterialModel | None:
        if (deck_dict := collection.find_one({'id': id})) is not None:
            deck: MaterialModel = MaterialModel(**deck_dict)

            return deck

        return None

    def update(self, id: str, deck: MaterialUpdateModel) -> bool | None:
        if (collection.find_one_and_update({'id': id}, {'$set': deck.dict()})) is not None:
            return True

        return None

    def delete(self, id: str) -> bool | None:
        if (collection.find_one_and_delete({'id': id})) is not None:
            return True

        return None


material = MaterialService()
