import importlib
from collections import deque
from copy import deepcopy

import minspider
from mongodao import taskmodel
from peristent.mongoperist import MongoPerist
from task.basecrawler import BaseCrawler


class TaskItem:
    def __init__(self, **kwargs):
        if 'url_items' in kwargs:
            kwargs['url_items'] = [minspider.UrlItem(**it) for it in kwargs['url_items'] ]
        self.__dict__.update(kwargs)

    def push_url_item(self, url_item: minspider.UrlItem):
        self.url_items.append(url_item)

    def get_dict(self):
        temp = deepcopy(self.__dict__)
        temp['url_items'] = [it.get_dict() for it in temp['url_items']]
        return temp


if __name__ == '__main__':

    task_list = taskmodel.get_all_tasks()
    deque_list = deque()
    t_task = [TaskItem(**item) for item in task_list]
    for item in t_task:
        mod_task = importlib.import_module('.' + item.task_cls, 'task')
        task_cls = [getattr(mod_task, it) for it in dir(mod_task) if not it.startswith('_') and hasattr(
            getattr(mod_task, it), '__base__') and getattr(mod_task, it).__base__ == BaseCrawler]
        for cls in task_cls:
            murl = minspider.UrlManager(deque([minspider.UrlItem(urlitem.url) for urlitem in item.url_items]))
            ins = cls(item, murl, MongoPerist())

            deque_list.append(ins)
    m = minspider.TaskManager(deque_list)
    m.do_task()
