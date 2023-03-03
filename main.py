# ToDo
# [ ] venv within docker
# [ ] motor_asyncio for async requests to database
# [ ] ObjectId

import os
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId
from config import Settings

class Customer(BaseModel):
    name: str
    address: str
    phone: str
    email: str | None = None


# Connect to MongoDB
# mongodb://localhost:27017/wquote-db
# mongodb+srv://usr_admin_rw:ZOh7rFTujTPvznV4@wquote-db.5wzf4ed.mongodb.net/test
settings = Settings()
client = MongoClient(settings.MONGODB_CONNECTION)
db = client["wquote"]
collection = db["customers"]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/customers/')
def get_customers():
    data = list(collection.find())

    for item in data:
        item['_id'] = str(item['_id'])

    print(f'opa nene: {data}')
    return data


@app.get('/customers/{id}')
def get_customer(id: str):
    data = collection.find_one({'_id': ObjectId(id)})
    data['_id'] = str(data['_id'])

    return data


@app.post('/customers/')
def create_customer(body: Customer):
    customer = dict(body)
    result = collection.insert_one(customer)

    if result.acknowledged:
        return collection.find_one({"_id": result.inserted_id}, {"_id": False})

    return None
