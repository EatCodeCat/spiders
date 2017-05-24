from urlmanager import UrlManager
from webspider import WebSpider
from bs4 import BeautifulSoup
from collections import Iterable
import traceback


class Crawler:
    def __init__(self, urlmanager):
        self.urlmanager = urlmanager
        self.headers = {}
        self.spider = WebSpider(self.headers)
        self.Soup = BeautifulSoup
        self.items = []
        self.cur_item = {}

    def docrawel(self):
        for urlitem in self.urlmanager:
            try:
                response = self.spider.get(urlitem.url)
                items = self.parse(response)
                if isinstance(items, Iterable):
                    for it in items:
                        self.items.append(it)
            except Exception as e:
                exstr = traceback.format_exc()
                print(exstr)
                self.urlmanager.cur_url_is_fail()
        return self.items

    def request(self, url,  callback, method='GET'):
        response = self.spider.get(url)
        if hasattr(callback, '__call__'):
            return callback(response)
        else:
            return response

    def parse(self, response):
        bs = self.Soup(response.text, 'lxml')
        return bs

    def response_txt_soup(self, response):
        bs = self.Soup(response.text, 'lxml')
        return bs

    def get_arr_frist_el(self, arr):
        if len(arr) > 0:
            return arr[0]
        return {'string': ''}
