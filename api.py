import datetime   # This will be needed later
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util
import json
from flask import Flask, request, redirect

app = Flask(__name__)

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

def getData():
    data = list(collection.find())
    data = {item['id']:item for item in data}
    return data

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        pass
    else:
        data = getData()
        data = parse_json(data)
        return data 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    