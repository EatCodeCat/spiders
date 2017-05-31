import re
from datetime import datetime

from minspider import Crawler


class JandanImageCrawler(Crawler):
    def __init__(self, name, lv, urlmanager, perist):
        self.lv = lv
        self.name = name
        self.__host__ = 'http://jandan.net/'
        self.headers = {
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
        super().__init__(urlmanager, perist)

    def parse(self, response):
        soup = super().parse(response)
        list = soup.select("#comments .commentlist li")

        sList = []
        for li in list:
            a = li.find(class_='view_img_link')
            img = li.find('img')
            timeStr = li.find(class_='author').find('a').string.lower();
            m = re.match(r'@(\d+) month ago', timeStr)
            cdate = datetime.now()
            if m is not None:
                cdate = cdate.replace(month=cdate.month - int(m.group(1)))
            else:
                m = re.match(r'/i@(\d+) days ago', timeStr)
                if m is not None:
                    cdate = cdate.replace(day=cdate.day - int(m.group(1)));
                else:
                    m = re.match(r'/i@(\d+) hours ago', timeStr)
                    if m is not None:
                        cdate = cdate.replace(day=cdate.day - int(m.group(1)));
                    else:
                        m = re.match(r'/i@(\d+) mins ago', timeStr)
                        if m is not None:
                            cdate = cdate.replace(minute=cdate.minute - int(m.group(1)));
                        else:
                            m = re.match(r'/i@(\d+) weeks ago', timeStr)
                            if m is not None:
                                cdate = cdate.replace(day=cdate.day - int(m.group(1)) * 7);

            thumbnail = img['src']
            mainPic = a['href']

            if thumbnail.endswith('gif'):
                mainPic = thumbnail.replace('thumb180', 'mw690')

            item = {
                'list_url': response.url,
                'warning_lv': self.lv,
                'title': '',
                'author': self.name,
                'thumbnail': thumbnail,
                'mainPic': mainPic,
                'tag': '',
                'from_website': self.__host__,
                'create_time': datetime.now(),
                'play_count': 0,
                'desc': '',
                'content_time': cdate
            }
            sList.append(item)
        return sList
