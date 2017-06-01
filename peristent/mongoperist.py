from minspider.peristent import Peristenter
from mongodao import mongoclient, taskmodel


class MongoPerist(Peristenter):
    def __init__(self):
        super().__init__()
        self.contents_dao = mongoclient.MClient('mini_show_db', 'contents')
        self.task_dao = taskmodel.task_dao

    def item_save(self, item: dict):
        self.contents_dao.insert_one(item)

    def url_item_save(self, task_item):
        taskmodel.insert_one(task_item)
