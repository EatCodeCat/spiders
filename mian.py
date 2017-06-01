import importlib
from collections import deque
from copy import deepcopy

import minspider
from mongodao import taskmodel
from peristent.mongoperist import MongoPerist
from task.basecrawler import BaseCrawler


class TaskItem:
    def __init__(self, _id, task_name: str, task_cls: str, url_items=[], host='', status=0, remark='', headers={},
                 interval='',
                 loop_type='', lv=0):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def push_url_item(self, url_item: minspider.UrlItem):
        self.url_items.append(url_item)

    def get_dict(self):
        temp = deepcopy(self.__dict__)
        temp['url_items'] = [it.get_dict() for it in temp['url_items']]
        return temp


if __name__ == '__main__':
    tlist = deque(
        [c for c in [TaskItem(None, '煎蛋', 'imagespider', [minspider.UrlItem('http://jandan.net/ooxx/page-55')])]])
    deque_list = deque()
    for item in tlist:
        mod_task = importlib.import_module('.' + item.task_cls, 'task')
        task_cls = [getattr(mod_task, it) for it in dir(mod_task) if not it.startswith('_') and hasattr(
            getattr(mod_task, it), '__base__') and getattr(mod_task, it).__base__ == BaseCrawler]
        for cls in task_cls:
            murl = minspider.UrlManager(deque([minspider.UrlItem(urlitem.url) for urlitem in item.url_items]))
            ins = cls(item, murl, MongoPerist())
            deque_list.append(ins)

    m = minspider.TaskManager(deque_list)
    m.do_task()
