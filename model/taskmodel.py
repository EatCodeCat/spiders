
from mongodao import mongoclient
task_dao = mongoclient.MClient('mini_task_db', 'url_tasks')

crawl_task = {
    'urlitem': [{
        'url': '',
        'referer': '',
        'crawl_time': '',
        'pre_crawl_time': '',
        'crawl_count': 0,
        'interval': '',
        'remark': ''

    }],
    'task_name': '',
    'task_id': '',
    'create_time': '',
    'host': '',
    'remark': '',
    'headers': {},
    'interval': '',
    'loop_type': 0 #重复类型 0 间隔时间，1，定点时间重复
}

def insert_one(item):
    task_dao.insert_one(item)

def insert_urlitem(taskId):
    task_dao.find_(item)

def get_all_tasks():
    return task_dao.find()




