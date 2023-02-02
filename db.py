import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["firstDB"]

print(db.list_collection_names)