from collections import deque
import log
from enum import Enum
from datetime import datetime


class CrawlStatus(Enum):
    uncrawl = 1
    fail = 2
    success = 0


class UrlItem:
    def __init__(self, url, crawl_count=0, status=CrawlStatus.uncrawl, crawl_time=None, taskcls=''):

        self.url = url
        self.crawl_time = crawl_time
        self.crawl_count = crawl_count
        self.status = status
        self.taskcls = taskcls

    def __eq__(self, other):
        if isinstance(other, UrlItem):
            return self.url == other.url
        else:
            return False

    def get_dict(self):
        self.__dict__['status'] = self.__dict__['status'].value
        return self.__dict__


class UrlManager:
    def __init__(self, crawllist=deque(), name='', reportprocess=True):
        self.crawllist = crawllist
        self.failcrawlist = []
        self.sucesscrawlist = []
        self.name = name
        self.curUrl = None
        self.reportprocess = reportprocess
        self.log = log
        self.is_fail = False

    def push_crawlurl(self, url_item):

        if url_item not in self.crawllist:
            self.crawllist.append(url_item)
            return True
        else:
            return False

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        if not self.is_fail:
            self.sucesscrawlist.append(self.curUrl)

        length = len(self.crawllist)
        if length > 0:
            self.curItem = self.crawllist.popleft()
            self.curItem.crawl_count += 1
            self.curItem.crawl_time = datetime.now()

            if self.reportprocess:
                log.logmsg('index (%s)-%s' % (length, self.curItem.url))

            return self.curItem
        else:
            raise StopIteration()

    def cur_url_is_fail(self):
        self.curItem.status = CrawlStatus.fail
        self.failcrawlist.append(self.curItem)
        self.is_fail = True

    def repeat_cur_url(self):
        self.crawllist.append(self.curUrl);

    def done(self):
        log.logmsg(self.name + ':done')
        return self.sucesscrawlist + self.failcrawlist


if __name__ == '__main__':
    print(UrlItem('aa').getdict())
