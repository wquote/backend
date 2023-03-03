from pymongo import MongoClient
from config import Settings


settings = Settings()


class DatabaseMongo:
    client = MongoClient(settings.MONGODB_CONNECTION)
    db = client["wquote"]
