"""
    MongoDB
        stores data as collections and documents
        collection is table
        document is record which is basically a JSON :)

    CRUD Operations

    Install the library pymongo

    Reference Documentation for pymongo with tutorials to explore -> https://pymongo.readthedocs.io/en/stable/tutorial.html
"""

import pymongo
print(pymongo.__version__)

# URL Encoding needs to be done before we connect -> https://www.urlencoder.org/

# Create Connection to MongoDB
# url = "mongodb+srv://atpl:atpl71177@cluster0.eh8zx.gcp.mongodb.net/auridb?retryWrites=true&w=majority"
# encoded_url = "mongodb%2Bsrv%3A%2F%2Fatpl%3Aatpl71177%40cluster0.eh8zx.gcp.mongodb.net%2Fauridb%3FretryWrites%3Dtrue%26w%3Dmajority"

url = "mongodb://atpl:atpl71177@cluster0-shard-00-00.eh8zx.gcp.mongodb.net:27017,cluster0-shard-00-01.eh8zx.gcp.mongodb.net:27017,cluster0-shard-00-02.eh8zx.gcp.mongodb.net:27017/auridb?ssl=true&replicaSet=atlas-f8rvp5-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(url)

print("Client Connected")

# Obtain Reference to the DataBase
# db = client.auridb
db = client['auridb']

print("Reference to DB Obtained")

# listing the collections
collections = db.list_collection_names()
print("Collections:", collections)

# Refer to a collection in the database
collection = db["students"]

print("Reference to collection students Obtained")

# Insert Operation
"""
student = {"roll": 301, "name": "Dave", "email": "dave@example.com"}
document = collection.insert_one(student)
print("Document Inserted:", document)
print("Document ID:", document.inserted_id)
"""

# Fetch Operation

# data = collection.find()
# print(data)
# # print(data.count())
# # print(data.next())
# for i in range(data.count()):
#     print(data.next())

# query = {"roll": 201}
query = {"roll": {"$gt": 200}}
# data = collection.find(query)
# data = collection.find(query).sort("name")
data = collection.find(query).sort("name", -1)
for document in data:
    print(document)

# Delete Operation
# query = {"roll": 201}
# result = collection.delete_one(query)
# print("Document Deleted:", result.deleted_count)

# deleting the entire collection
# collection.drop()

# Update Document
query = {"roll": 301}
student_data = {"$set": {"name": "Dave Watson", "email": "dave.watson@example.com"}}
result = collection.update_one(query, student_data)
print("Data Updated:", result.modified_count)