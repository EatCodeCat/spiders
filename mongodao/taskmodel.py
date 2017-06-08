from mongodao import mongoclient

task_dao = mongoclient.MClient('mini_task_db', 'crawl_tasks')

crawl_task = {
    'urlitems': [{
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
    'loop_type': 0  # 重复类型 0 间隔时间，1，定点时间重复
}


def insert_one(item):
    task_dao.insert_one(item)


def get_all_tasks():
    return task_dao.find()


def get_task_by_id(id):
    return task_dao.find_one(_id=task_dao.ObjectId(id))


def update(id, model):
    model["_id"] = task_dao.ObjectId(model["_id"])
    return task_dao.update(model, _id=task_dao.ObjectId(id))


def search_tasks(index, page, **filter):
    return task_dao.search(index, page)


def find_one_and_replace(condit, replace):
    return task_dao.find_one_and_replace(condit, replace)


def delete(id):
    return task_dao.delete(task_dao.ObjectId(id))
