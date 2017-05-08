# coding=utf-8
__author__ = 'think'
import requests


class WebSpider:
    def __init__(self, headers):
        self.headers = {
            'accept-encoding': 'gzip, deflate, sdch, br',
            'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,nb;q=0.2,sk;q=0.2,zh-TW;q=0.2',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' +
                          ' Chrome/57.0.2987.98 Safari/537.36'
        }
        self.headers = dict(self.headers, **headers)


    def get_text(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def set_headers(self, item):
        self.headers = dict(self.headers, **item)

