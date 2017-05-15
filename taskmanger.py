# coding=utf-8
__author__ = 'think'
from wechatcrawler import WebcatCrawler

from imagespider import JandanImageCrawler

from mongodao import mongoclient

contents_dao = mongoclient.MClient('mini_show_db', 'contents')

image_ontents_dao = mongoclient.MClient('mini_show_db', 'image_contents')


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

def craw_all_jandanimage_task():
    jdcrawler = JandanImageCrawler('煎蛋网-妹子图', 6)
    for i in range(10, 58):
        url = 'http://jandan.net/ooxx/page-' + str(i)
        print(url)
        list = jdcrawler.do_crawle(url)
        for it in list:
            it['list_url'] = url
            image_ontents_dao.insert_one(it)


if __name__ == '__main__':
    craw_all_jandanimage_task()
