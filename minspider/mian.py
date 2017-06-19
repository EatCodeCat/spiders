import importlib
from collections import deque
from copy import deepcopy

import minspider
from mongodao.taskmodel import TaskModel
from taskperistent.mongoperist import MongoPerist
from task.basecrawler import BaseCrawler


class TaskItem:
    def __init__(self, **kwargs):
        if 'url_items' in kwargs:
            kwargs['url_items'] = [minspider.UrlItem(**it) for it in kwargs['url_items']]
        self.__dict__.update(kwargs)
        self.taskmodel = TaskModel()

    def push_url_item(self, url_item: minspider.UrlItem):
        self.url_items.append(url_item)

    def get_dict(self):
        temp = deepcopy(self.__dict__)
        temp['url_items'] = [it.get_dict() for it in temp['url_items']]
        return temp

    def save_update(self):
        if '_id' in self.get_dict():
            self.taskmodel.replace_one(self.get_dict()['_id'], self.get_dict())
        else:
            self.taskmodel.insert_one(self.get_dict())



def execute_all():
    taskmodel = TaskModel()
    task_list = taskmodel.get_all_tasks()

    t_task = [TaskItem(**item) for item in task_list]
    deque_list = deque()
    for item in t_task:
        deque_list += build_task(item)
    m = minspider.TaskManager(deque_list)
    m.do_task()
    return m

def execute_one(item):
    deque_list = deque()
    deque_list += build_task(item)
    m = minspider.TaskManager(deque_list)
    m.do_task()
    return m

def build_task(item, module='task'):
    deque_list = deque()
    mod_task = importlib.import_module('.' + item.task_cls, module)
    task_cls = [getattr(mod_task, it) for it in dir(mod_task) if not it.startswith('_') and hasattr(
        getattr(mod_task, it), '__base__') and getattr(mod_task, it).__base__ == BaseCrawler]
    for cls in task_cls:
        murl = minspider.UrlManager(deque([minspider.UrlItem(urlitem.url) for urlitem in item.url_items]))
        ins = cls(item, murl, MongoPerist())
        deque_list.append(ins)
    return deque_list

if __name__ == "__main__":
    execute_all()
