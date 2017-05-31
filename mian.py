from collections import deque
from model import taskmodel
import importlib
import minspider
import task

tlist = deque([c for c in taskmodel.get_all_tasks()])


class TaskItem:
    def __init__(self, task_name: str, task_id: str, host: str, status: int, remark: str, headers: dict, interval: str,
                 loop_type: int, lv: int, urlitems: list):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


if __name__ == '__main__':

    deque_list = deque()
    for item in tlist:
        mod_task = importlib.import_module('.' + item['task_id'], 'task')
        task_cls = [getattr(mod_task, it) for it in dir(mod_task) if not it.startswith('_') and hasattr(
            getattr(mod_task, it), '__base__') and getattr(mod_task, it).__base__ == minspider.Crawler]
        for cls in task_cls:
            murl = minspider.UrlManager(deque([minspider.UrlItem(urlitem['url']) for urlitem in item['urlitems']]))
            ins = cls(item['task_name'], item['lv'], murl, minspider.Peristenter())
            deque_list.append(ins)

    m = minspider.TaskManager(deque_list)
    m.do_task()
