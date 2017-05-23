from collections import deque


class UrlManager:
    def __init__(self, name, collection, reportprocess, log):
        self.crawllist = deque()
        self.failcrawlist = []
        self.name = name
        self.curUrl = None
        self.reportprocess = reportprocess
        self.collection = collection
        self.log = log

    def initdata(self, *urls):
        '''
        读取要爬取的url
        :return: 
        '''
        pass

    def pushCrawlUrl(self, url):
        i = self.crawllist.index(url)
        if i == -1:
            self.crawllist.append(url)
            return True
        else:
            return False

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        length = len(self.crawllist)
        if length > 0:
            self.curUrl = self.crawllist.popleft()

            if self.reportprocess:
                self.log.print('index (%)-%s'.format(length, self.curUrl))

            return self.curUrl
        else:
            raise StopIteration()

    def cururlisfail(self):
        self.failcrawlist.append(self.curUrl)

    def done(self):
        '''
        保存状态
        :return: 
        '''
        pass
