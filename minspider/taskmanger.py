from concurrent.futures import ThreadPoolExecutor
from .crawler import Crawler
import collections
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from copy import deepcopy
import minspider
from collections import deque
from mongodao.taskmodel import TaskModel

class TaskItem:
    def __init__(self, **kwargs):
        if 'url_items' in kwargs:
            kwargs['url_items'] = [minspider.UrlItem(**it) for it in kwargs['url_items']]
            self.url_manager = minspider.UrlManager(deque(kwargs['url_items']))
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



class TaskManager:
    def __init__(self, deque_task: collections.deque, max_workers=10):
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.deque_task = deque_task
        self.sched = BlockingScheduler()

    def do_task(self):
        for task in self.deque_task:
            self.add_job(task)
        self.sched.start()

    def add_job(self, task):
        if isinstance(task, Crawler):
            # 立即执行
            if  not hasattr(task.task_item, 'loop_type') or task.task_item.loop_type == 1:
                task.do_crawl()
            # 按时间执行
            elif task.task_item.loop_type == 2:
                run_date = datetime.datetime.strptime(task.task_item.exec_time, '%yyyy-%mm-%dd %HH:%MM:%SS')
                self.sched.add_job(task.do_crawl, 'date', run_date=run_date)
            else:
                cron_dict = self.parse_cron_str(task.task_item.cron)
                self.sched.add_job(task.do_crawl, 'cron', **cron_dict)
        else:
            raise TypeError('task must inherit Crawler')

    def parse_cron_str(self, cron_str: str):
        year, month, day, week, day_of_week, hour, minute, second, start_date, end_date = cron_str.split(' ')
        return {
            'year': year,
            'month': month,
            'day ': day,
            'week': week,
            'day_of_week': day_of_week,
            'hour': hour,
            'minute': minute,
            'second': second,
            'start_date': start_date,
            'end_date': end_date
        }
