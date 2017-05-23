
from urlmanager import  UrlManager
from  webspider import WebSpider
from bs4 import BeautifulSoup

class Crawler:

    def init(self):
        self.urlmanager = UrlManager()
        self.headers = {}
        self.spider = WebSpider(self.headers)
        self.Soup = BeautifulSoup;




    def docrawel(self):
        pass


    def parse(self, response):
        pass


