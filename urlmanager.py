from collections import deque
import log


class UrlItem:
    '''
        status 0 成功， 1 未爬取， 2 失败
    '''

    def __init__(self, url, crawl_count=0, status=1, crawl_time=None):

        self.url = url
        self.crawl_time = crawl_time
        self.crawl_count = crawl_count
        self.status = status

    def __eq__(self, other):
        if isinstance(other, UrlItem):
            return self.url == other.url
        else:
            return False


class UrlManager:
    def __init__(self, name, crawllist=deque(), reportprocess=True):
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

            if self.reportprocess:
                log.logmsg('index (%s)-%s' %(length, self.curItem.url))

            return self.curItem
        else:
            log.logmsg(self.name + ':done')

            raise StopIteration()

    def cur_url_is_fail(self):
        self.failcrawlist.append(self.curUrl)
        self.is_fail = True

    def repeat_cur_url(self):
        self.crawllist.append(self.curUrl);

    def done(self):
        return self.sucesscrawlist, self.failcrawlist


if __name__ == '__main__':
    pass
