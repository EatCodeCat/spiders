# coding=utf-8
__author__ = 'think'

import pymongo


class MClient:
    def __init__(self, db, collection):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db]
        self.collection = self.db[collection]

    def insert_one(self, entity):
        self.collection.insert_one(entity)
    
    def find(self):
        return self.collection.find()

    def search(self, index, page, **filter):
        return self.collection.find(filter, skip= page*index, limit=page)

    def find_one_and_replace(self, ceritira,repacement):
        return self.collection.insert_one(filter=ceritira, replacement=repacement)


