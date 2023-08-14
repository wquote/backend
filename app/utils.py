
from uuid import uuid4


def generate_uuid4() -> str | None:
    return str(uuid4())


# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


# Recebe um dict, converte o atributo com ObjectId para string, e retorna um dict
def decodeObjId(item_dict: dict) -> dict:
    # item_dict = json.loads(JSONEncoder().encode(item_dict))
    item_dict['id'] = str(item_dict.pop('_id'))
    # item_dict = {('id' if k == '_id' else k): (str(v) if isinstance(v, ObjectId) else v) for (k, v)
    #  in item_dict.items()}

    return item_dict
