from minspider import Crawler


class BaseCrawler(Crawler):
    def __init__(self, task_item, urlmanager, perist):
        self.lv = task_item['lv']
        self.urlmanager = urlmanager
        self.name = task_item['task_name']
        self.__host__ = task_item['host']
        self.task_item = task_item
        super().__init__(urlmanager, perist)

    def url_item_persistence(self, items):
        self.task_item['url_items'] = [it.get_dict() for it in items]
        print('保存task')
        super().url_item_persistence(self.task_item)
