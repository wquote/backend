from typing import List
from app import services
from app.models.material import MaterialModel, MaterialUpdateModel


class MaterialBusiness():
    def create(self, material: MaterialModel) -> str | None:
        material_id: str | None = services.material.create(material)

        return material_id if material_id is not None else None

    def read_all(self) -> List[MaterialModel]:
        materials: List[MaterialModel] = services.material.read_all()

        return materials

    def read(self, id: str) -> MaterialModel | None:
        material: MaterialModel | None = services.material.read(id)

        return material if material is not None else None

    def update(self, id: str, material: MaterialUpdateModel) -> bool | None:
        if (services.material.update(id, material)):
            return True

        return None

    def delete(self, id: str):
        if (services.material.delete(id)):
            return True

        return None


material = MaterialBusiness()
