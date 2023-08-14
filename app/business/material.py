from typing import List
from app import services
from app.models.material import Material, MaterialCreate, MaterialUpdate


class MaterialBusiness():
    def create(self, material: MaterialCreate) -> str | None:
        material_id: str | None = services.material.create(material)

        return material_id if material_id is not None else None

    def read_all(self) -> List[Material]:
        materials: List[Material] = services.material.read_all()

        return materials

    def read(self, id: str) -> Material | None:
        material: Material | None = services.material.read(id)

        return material if material is not None else None

    def update(self, id: str, material: MaterialUpdate) -> bool | None:
        if (services.material.update(id, material)):
            return True

        return None

    def delete(self, id: str):
        if (services.material.delete(id)):
            return True

        return None


material = MaterialBusiness()
