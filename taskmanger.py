# coding=utf-8
__author__ = 'think'
from wechatcrawler import WebcatCrawler, persistent
from imagespider import JandanImageCrawler
from mongodao import mongoclient
from urlmanager import UrlManager,UrlItem

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
    'remark': '',
    'headers': {},
    'interval': '',
    'loop_type': 0 #重复类型 0 间隔时间，1，定点时间重复
}


def crawl_all_wechat_task():

    murl = UrlManager('麦格时光')
    for i in range(1, 22):
        if (i > 1):
            url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889-' + str(i) + '.html'
        else:
            url = 'http://wx.abbao.cn/wu/89d90ad43c9e4889.html'
        murl.push_crawlurl(UrlItem(url))

    wc = WebcatCrawler('麦格时光', 0, murl)
    list = wc.docrawel()
    print (len(list))
    #persistent(list)


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
    crawl_all_wechat_task()
