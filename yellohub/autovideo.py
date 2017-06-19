# coding=utf-8
__author__ = 'think'
import  minspider
import basecrawler


class AutoVideoCrawler(minspider.Crawler):

    def __init__(self):
        self.host = 'http://www.aotu17.com/'


        super().__init__()

    def detail_parser(self, response):
        pass

    def parse(self, response):
        soup = super().parse(response)
        videos = soup.select('.videos')
        for video in videos:
            a = self.get_arr_frist_el(video.select('.video a'))['href']
            print (a)