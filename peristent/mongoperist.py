from peristent import Peristenter
from mongodao import mongoclient


class MongoPerist(Peristenter):
    def __init__(self):
        super().__init__()
        self.contents_dao = mongoclient.MClient('mini_show_db', 'contents')

    def item_save(self, item: dict):
        self.contents_dao.insert_one(item)
