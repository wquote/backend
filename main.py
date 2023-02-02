# ToDo
# [ ] venv within docker
# [ ] motor_asyncio for async requests to database
# [ ] ObjectId

from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId


class Customer(BaseModel):
    name: str
    address: str
    phone: str
    email: str | None = None


# Connect to MongoDB
client = MongoClient("mongodb://wquote-db:27017/")
db = client["wquote"]
collection = db["customers"]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/customers/')
def get_customers():
    data = list(collection.find({}, {'_id': False}))
    return data


@app.get('/customers/{id}')
def get_customer(id: str):
    data = collection.find_one({'_id': ObjectId(id)}, {'_id': False})
    return data


@app.post('/customers/')
def create_customer(body: Customer):
    customer = dict(body)
    result = collection.insert_one(customer)

    if result.acknowledged:
        return collection.find_one({"_id": result.inserted_id}, {"_id": False})

    return None
