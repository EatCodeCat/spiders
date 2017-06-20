# coding=utf-8
__author__ = 'think'
import minspider
from yellohub.basecrawler import BaseCrawler
from  collections import deque


class AotuVideoCrawler(minspider.Crawler):
    def __init__(self):
        self.host = 'http://www.aotu17.com/'

        self.urlmanager = minspider.UrlManager(deque(['http://www.aotu17.com/']))
        self.task_item = minspider.TaskItem()
        super().__init__(self.urlmanager)

    def detail_parser(self, response):
        pass

    def parse(self, response):
        soup = super().parse(response)
        videos = soup.select('.videos')
        for video in videos:
            a = self.get_arr_frist_el(video.select('.video a'))['href']
            print(a)
