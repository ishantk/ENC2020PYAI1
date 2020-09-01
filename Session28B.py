import pymongo

class DB:

    def __init__(self, collection):
        url = "mongodb://atpl:atpl71177@cluster0-shard-00-00.eh8zx.gcp.mongodb.net:27017,cluster0-shard-00-01.eh8zx.gcp.mongodb.net:27017,cluster0-shard-00-02.eh8zx.gcp.mongodb.net:27017/auridb?ssl=true&replicaSet=atlas-f8rvp5-shard-0&authSource=admin&retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        db = client['auridb']
        # Refer to a collection in the database
        self.collection = db[collection]
        print("MongoDB Connection Obtained")

    def add_customer(self, customer):
        document = self.collection.insert_one(customer)
        print("Customer Added:", document.inserted_id)

    def delete_customer(self):
        pass

    def update_customer(self):
        pass

    def fetch_customers(self):
        pass