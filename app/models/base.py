
# referência: https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/

from bson import ObjectId
from pydantic import fields


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError('Invalid ObjectId')
        return cls(value)


class ObjectIdField(fields.ModelField):
    def __init__(self, **kwargs):
        super().__init__(alias='_id', **kwargs)

    # Override the prepare method to convert ObjectId to str
    def prepare(self, value):
        if isinstance(value, ObjectId):
            return ObjectIdStr(str(value))
        return value
