from typing import Dict, List
from app.material.material_service import material_service
from app.shared.base_repository import BaseRepository, raise_error
from app.utils import decodeObjId


class DmoRepository(BaseRepository):
    def __init__(self, collection: str, dto):
        super().__init__(collection, dto)

    def read_all(self) -> List[Dict]:
        try:
            items_list: List[Dict] = list(self.collection.find())
            for item in items_list:
                for material in item["materials"]:
                    read_material = material_service.read(material["id"])
                    material["name"] = read_material.desc

            items = [self.dto(**decodeObjId(i)) for i in items_list]

        except Exception as e:
            raise_error(e)

        return items
