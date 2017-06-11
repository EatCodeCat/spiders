from concurrent.futures import ThreadPoolExecutor
from .crawler import Crawler
import collections
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


class TaskManager:
    def __init__(self, deque_task: collections.deque, max_workers=10):
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.deque_task = deque_task
        self.sched = BlockingScheduler()

    def do_task(self):
        for task in self.deque_task:
            if isinstance(task, Crawler):
                # 立即执行
                if task.task_item.loop_type == 1:
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
        self.sched.start()

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


if __name__ == '__main__':
    manager = TaskManager()
    manager.do_task()
