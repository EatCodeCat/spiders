from  webspider import WebSpider
from bs4 import BeautifulSoup

import re
from datetime import datetime
from datetime import date

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,nb;q=0.2,sk;q=0.2,zh-TW;q=0.2",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "jdna=01b0531fab6a989460dd1b231010b496#1494847995867; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1494847996; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1494847996; _ga=GA1.2.1493398848.1494847997; _gid=GA1.2.446729764.1494847997",
    "Host": "jandan.net",
    "Referer": "http://jandan.net/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
}


class JandanImageCrawler:
    def __init__(self, name, lv):
        self.lv = lv
        self.name = name
        self.spider = WebSpider(headers)
        self.__host__ = 'http://jandan.net/'

    # // wx2.sinaimg.cn / thumb180 / 63861
    # dc0gy1ffm5l7eve6g209q069qv5.gif
    # // wx2.sinaimg.cn / mw690 / 63861
    # dc0gy1ffm5l7eve6g209q069qv5.gif
    def do_crawle(self, url):
        list = self.imgecrawler(url)
        return list;

    def imgecrawler(self, url):
        text = self.spider.get_text(url);
        soup = BeautifulSoup(text, 'lxml');
        list = soup.select("#comments .commentlist li p");
        for li in list:
            a = li.find('a')
            img = li.find('img')
            print(a['href'], img['src'])


if __name__ == '__main__':
    jd = JandanImageCrawler('煎蛋网', 3)
    jd.do_crawle('http://jandan.net/ooxx/page-55')
