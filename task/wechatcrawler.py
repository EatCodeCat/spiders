# coding=utf-8
__author__ = 'think'
import re
from datetime import date
from datetime import datetime

from mongodao import mongoclient
from task.basecrawler import BaseCrawler

date_pattern = re.compile(r'(\d+)月(\d+)日')


class WebcatCrawler(BaseCrawler):
    '''
    爬取 wx.abbao.cn站点的微信公众号
    '''
    def __init__(self, task_item, urlmanager, perist):
        super().__init__(task_item, urlmanager, perist)
        self.headers = {
            'referer': 'http://wx.abbao.cn/wu/89d90ad43c9e4889.html',
            'Host': 'wx.abbao.cn',
            'Upgrade-Insecure-Requests': "1",
            'cookie': '__cfduid=d6ba247ce04c41e697a314f8ae7b86f471493906917; Hm_lvt_58ea004dc0522057209aba54c622e023=1493906904; Hm_lpvt_58ea004dc0522057209aba54c622e023=1493906904; __utma=143276005.667657622.1493906905.1493906905.1493906905.1; __utmc=143276005; __utmz=143276005.1493906905.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_5a0dc5f0063da06a17d0ae7f64c9d1c6=1493909038; Hm_lpvt_5a0dc5f0063da06a17d0ae7f64c9d1c6=1493911728'
        }

    def detail_parser(self, response):
        soup = self.response_txt_soup(response)
        content = soup.find(id='js_content')
        return str(content)

    def parse(self, response):
        soup = super().parse(response)
        itemList = soup.select('.uk-width-medium-3-4 .rel-articles  .article-item')
        for item in itemList:
            a = item.select('h4 a')
            title = self.get_arr_frist_el(a).string
            detailUrl = self.get_arr_frist_el(a)['href']
            c_date = self.get_arr_frist_el(item.select('h4 .ext')).string
            desc = self.get_arr_frist_el(item.select('.wx-news-ext')).string
            thumbnail = self.get_arr_frist_el(item.select('.cover-wrap img'))["data-src"]

            if (c_date):
                m = date_pattern.match(c_date)

                if m:
                    month, d = m.group(1, 2)
                    c_date = date(date.today().year, int(month), int(d))
                    c_date = datetime.strptime(str(c_date), '%Y-%m-%d')
                else:
                    m = re.match(r'(\d +)小时前', c_date)
                    if (m):
                        c_date = date.today()
                        c_date = datetime.strptime(str(c_date), '%Y-%m-%d').utcnow()
            if (not detailUrl.startswith('https://') and not detailUrl.startswith('http://')):
                detailUrl = self.__host__ + detailUrl

            self.cur_item = {
                'content_type': 1,
                'title': title,
                'thumbnail': thumbnail,
                'warning_lv': self.warnning_lv,
                'desc': desc,
                'author': self.name,
                'content_time': c_date,
                'list_url': '',
                'detail_url': detailUrl,
                'from_website': self.__host__,
            }
            detail_txt = self.request('http://'+detailUrl, self.detail_parser)
            self.cur_item['content'] = detail_txt
            yield self.cur_item

    def item_persistence(self, items):
        contents_dao = mongoclient.MClient('mini_show_db', 'contents')
        for it in items:
            contents_dao.insert_one(it)
