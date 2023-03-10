import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# Adding a new record:
# new_doc = {"first":"Stuff", "last":"things", "key":"value", "JSON":"Format"}
# coll.insert_one(new_doc)

# Adding multiple in one go - Use an Array of dictionaries:
"""
new_docs = [{
    "first":"name",
    "last":"name",
    "same":"format"
}, {
    "first":"name",
    "last":"name",
    "same":"format"
}
]
"""

coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)