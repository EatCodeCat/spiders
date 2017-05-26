# coding=utf-8
__author__ = 'think'
# from wechatcrawler import WebcatCrawler, persistent
from imagespider import JandanImageCrawler
from mongodao import mongoclient
from urlmanager import UrlManager, UrlItem
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import time
import task
from task.crawler import Crawler
import importlib
from model import taskmodel


contents_dao = mongoclient.MClient('mini_show_db', 'contents')
image_ontents_dao = mongoclient.MClient('mini_show_db', 'image_contents')

crawl_task = {
    'url': {
        'url': '',
        'referer': '',
        'crawl_time': '',
        'pre_crawl_time': '',
        'crawl_count': 0,
        'interval': '',
        'remark': ''

    },
    'task_name': '',
    'task_id': '',
    'create_time': '',
    'host': '',
    'status': '',
    'remark': '',

    'headers': {},
    'interval': '',
    'loop_type': 0  # 重复类型 0 间隔时间，1，定点时间重复
}


# def crawl_all_wechat_task():
#     murl = UrlManager('麦格时光')
#
#         murl.push_crawlurl(UrlItem(url))

#     wc = WebcatCrawler('麦格时光', 0, murl)
#     list = wc.docrawel()
#     persistent(list)


# def craw_all_jandanimage_task():
#     jdcrawler = JandanImageCrawler('煎蛋网-妹子图', 6)
#     for i in range(10, 58):
#         url = 'http://jandan.net/ooxx/page-' + str(i)
#         print(url)
#         list = jdcrawler.do_crawle(url)
#         for it in list:
#             it['list_url'] = url
#             image_ontents_dao.insert_one(it)

class TaskItem:
    def __init__(self, task_name, task_id, host, status, remark, headers, interval, loop_type, lv, urlitems):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


class TaskManager:
    def __init__(self, task_list=deque(), max_workers=10):
        self.task_list = deque([c for c in taskmodel.get_all_tasks()])
        self.pool = ThreadPoolExecutor(max_workers=max_workers)

    def do_task(self):
        for item in self.task_list:
            mod_task = importlib.import_module('.' + item['task_id'], 'task')
            tasklist = [it for it in dir(mod_task) if not it.startswith('_') and hasattr(
                getattr(mod_task, it), '__base__') and getattr(mod_task, it).__base__ == Crawler]
            for task in tasklist:
                murl = UrlManager(deque([UrlItem(urlitem['url']) for urlitem in item['urlitems']]))
                ins = getattr(mod_task, task)(item['task_name'], item['lv'], murl)
                th = self.pool.submit(ins.docrawel)
                list = th.result()
                ins.persistent(list)


if __name__ == '__main__':
    # urlitems = []

    # for i in range(1, 10):
    #         if (i > 1):
    #             url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889-' + str(i) + '.html'
    #         else:
    #             url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889.html'
    #         urlitems.append(UrlItem(url).get_dict())
    # task = TaskItem('麦格时光', 'wechatcrawler', 'http://wx.abbao.cn', 0, '', {}, '', 0, 0, urlitems).__dict__
    # print(task)
    # taskmodel.insert_one(task)
    manager = TaskManager()
    manager.do_task()
