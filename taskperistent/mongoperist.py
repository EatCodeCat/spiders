from minspider.peristent import Peristenter
from mongodao import mongoclient
from mongodao.taskmodel import TaskModel




class MongoPerist(Peristenter):
    def __init__(self):
        super().__init__()
        self.contents_dao = mongoclient.MClient('mini_show_db', 'contents')
        self.taskmodel = TaskModel()

    def item_save(self, item: dict):
        self.contents_dao.insert_one(item)

    def url_item_save(self, task_item: dict):
        self.taskmodel.replace_one(task_item["_id"],task_item)
