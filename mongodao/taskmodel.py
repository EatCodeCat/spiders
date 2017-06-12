from mongodao import mongoclient

task_dao = mongoclient.MClient('mini_task_db', 'crawl_tasks')


def insert_one(item):
    task_dao.insert_one(item)


def get_all_tasks():
    return task_dao.find()


def get_task_by_id(id):
    return task_dao.find_one(_id=task_dao.ObjectId(id))


def replace_one(id, model):
    model["_id"] = task_dao.ObjectId(model["_id"])
    return task_dao.replace_one(model, _id=task_dao.ObjectId(id))

def update_task(update, id):
    return task_dao.update(update, {'_id': task_dao.ObjectId(id)})

def search_tasks(index, page, **filter):
    return task_dao.search(index, page, **filter)


def find_one_and_replace(condit, replace):
    return task_dao.find_one_and_replace(condit, replace)

def delete(id):
    return task_dao.delete(task_dao.ObjectId(id))
