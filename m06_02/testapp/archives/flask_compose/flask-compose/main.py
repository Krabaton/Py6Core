from flask import Flask
import os
from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")

db = client.test

app = Flask(__name__)


@app.route("/")
def hello():
    result = {}
    data = db.users.find({})
    for el in data:
        result.update({f"{el.get('_id')}": el.get("name")})
    return result


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
