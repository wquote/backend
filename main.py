# ToDo
# [ ] venv within docker
# [ ] motor_asyncio for async requests to database
# [ ] ObjectId

from fastapi import FastAPI

from pydantic import BaseModel
from bson.objectid import ObjectId
from config import Settings
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:4201",
    "https://wquote.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connect to MongoDB
settings = Settings()
client = MongoClient(settings.MONGODB_CONNECTION)
db = client["wquote"]


class Customer(BaseModel):
    name: str
    address: str
    phone: str
    email: str | None = None


collection = db["customers"]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/customers/')
def readAll():
    data = list(collection.find())

    for item in data:
        item['_id'] = str(item['_id'])

    return data


@app.get('/customers/{id}')
def read(id: str):
    data = collection.find_one({'_id': ObjectId(id)})

    if data:
        data['_id'] = str(data['_id'])

        return data

    return None


@app.post('/customers/')
def create(body: Customer):
    body_dict = dict(body)
    result = collection.insert_one(body_dict)

    if result.acknowledged:
        data = collection.find_one({"_id": result.inserted_id})
        data['_id'] = str(data['_id'])

        return data

    return None


@app.put('/customers/{id}')
def update(id: str, body: Customer):
    body_dict = dict(body)
    data = collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': body_dict})

    if data:
        data['_id'] = str(data['_id'])
        return data

    return None


@app.delete('/customers/{id}')
def delete(id: str):
    data = collection.find_one_and_delete({'_id': ObjectId(id)})

    if data:
        data['_id'] = str(data['_id'])
        return data

    return None
