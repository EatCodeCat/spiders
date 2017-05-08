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


