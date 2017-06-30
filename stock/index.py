import json
import tushare as ts
from mongodao import stockmodel
from stock.mongodbscheduler import scheduler
from apscheduler import events


def basic_data():
    print('start')
    basic = ts.get_stock_basics()
    # data = json.loads(basic_data.to_json(orient='records'))
    for i in basic.index:
        item = basic.ix[i].to_dict()
        item['code'] = i
        item['timeToMarket'] = float(item['timeToMarket'])
        item['holders'] = float(item['holders'])
        stockmodel.BasicStockModel().replace_one(item, code=i)

    print('end')


def per_day_task():
    basic_data()


scheduler.add_job(basic_data)

def done(e):
    print('done')

scheduler.add_listener(done, events.EVENT_SCHEDULER_STARTED | events.EVENT_JOB_EXECUTED)

scheduler.start()


# 每天6点 爬取盘面数据
# 股票列表
# 股票行情
