
from pymongo import MongoClient
from dotenv import dotenv_values


dotenv = dotenv_values('.env')
client: MongoClient = MongoClient(dotenv['MONGODB_CONNECTION'])
db = client.get_database(dotenv['DB_NAME'])
