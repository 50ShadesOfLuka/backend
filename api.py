import datetime   # This will be needed later
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import json

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
db = client["epel"]
collection = db['epeldata']

# # Load mockdata into epeldata
# with open('EpelepData.json') as f:
#     file_data = json.load(f)
# collection.insert_many(file_data)

data = list(collection.find())

print(data)
