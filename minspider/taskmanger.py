from concurrent.futures import ThreadPoolExecutor
from .crawler import Crawler
import collections


class TaskManager:
    def __init__(self, deque_task: collections.deque, max_workers=10):
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.deque_task = deque_task

    def do_task(self):

        def task_done(_task, _th):
            _task.item_persistence(_th.result())

        for task in self.deque_task:
            if isinstance(task, Crawler):
                th = self.pool.submit(task.do_crawl)
            else:
                raise TypeError('task must inherit Crawler')

if __name__ == '__main__':
    manager = TaskManager()
    manager.do_task()
