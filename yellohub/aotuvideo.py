# coding=utf-8
__author__ = 'think'
import minspider
from  collections import deque
from mongodao.yellohubmodel import VideosModel
from datetime import datetime
import re


class AotuVideoCrawler(minspider.Crawler):
    def __init__(self):
        self.host = 'http://www.aotu17.com'

        template_url = 'http://www.aotu17.com/recent/%s/'

        url_arr = ['http://www.aotu17.com/']
        for i in range(2, 354):
            url_arr.append(template_url % i)

        self.urlmanager = minspider.UrlManager(deque(url_arr))
        self.task_item = minspider.TaskItem()
        self.dao = VideosModel()
        super().__init__(self.urlmanager)

    def detail_parser(self, response):
        soup = self.response_txt_soup(response)
        video = soup.find('video')
        self.item['poster'] = video['poster']
        source = video.select('source')
        standby = []
        for item in source:
            standby_item = {
                'src': item['src'],
                'label': item['label'],
                'res': item['res']
            }
            standby.append(standby_item)

        self.item['video_url_list'] = standby

        taglist = soup.select('#about-container .btn-margin')
        tagset = set()
        for tag in taglist:
            if tag.string is not None:
                tagset.add(tag.string)
        self.item['tag_list'] = list(tagset)

    def parse(self, response):
        soup = super().parse(response)
        panel = soup.select('.panel-body')
        if len(panel) > 0:
            if len(panel) > 2:
                videos = panel[2].select('.videos .video')
            else:
                videos = panel[0].select('.videos .video')

            for video in videos:
                a = self.get_arr_frist_el(video.select('a'))
                detailUrl = a['href']
                thumb_pic = a.find('img')['src']
                title = a.find(class_='video-title').string
                self.item = {
                    'detail': detailUrl,
                    'title': title,
                    'thumb_pic': thumb_pic,
                    'update_time': datetime.now()
                }
                print(detailUrl)
                self.request(self.host + detailUrl, self.detail_parser)
                self.items.append(self.item)
            return self.items


    def item_persistence(self, items):
        for item in items:
            self.dao.insert_one(item)


