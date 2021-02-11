import pymongo
import json


__author__ = 'Deepak'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["iqoption"]

    @staticmethod
    def insert_one(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def test_one(collection):
        return Database.DATABASE[collection].find_one({})

    @staticmethod
    def update_one(collection, record_id, data):
        Database.DATABASE[collection].update_one({'_id': record_id}, {"$set": data}, upsert=False)


