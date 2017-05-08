# coding=utf-8
__author__ = 'think'
from wechatcrawler import WebcatCrawler

from  mongodao import mongoclient

contents_dao = mongoclient.MClient('mini_show_db', 'contents')


def crawl_all_wechat_task():
    wc = WebcatCrawler('麦格时光', 0)
    for i in range(1, 22):
        if (i > 1):
            url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889-' + str(i) + '.html'
        else:
            url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889.html'
        list = wc.do_crawle(url)
        for it in list:
            it['list_url'] = url
            contents_dao.insert_one(it)


crawl_all_wechat_task()