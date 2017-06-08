# coding=utf-8
__author__ = 'think'

import pymongo
from bson.objectid import ObjectId


class MClient:
    def __init__(self, db, collection):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db]
        self.collection = self.db[collection]

    def insert_one(self, entity):
        self.collection.insert_one(entity)

    def ObjectId(self, _id):
        return ObjectId(_id)

    def find(self):
        return self.collection.find()

    def find_one(self, **filter):
        return self.collection.find_one(filter)

    def update(self, repacement, **filter):
        return self.collection.replace_one(filter, repacement)

    def search(self, index, page, **filter):
        count = self.collection.count(filter)
        cursor = self.collection.find(filter, skip=page * index, limit=page)
        return  cursor, count

    def delete(self, _id):
        return self.collection.delete_one({"_id": _id})
