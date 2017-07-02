import json
import tushare as ts
from mongodao import stockmodel
from stock.mongodbscheduler import scheduler
from apscheduler import events

basic_model = stockmodel.BasicStockModel()

k_model = stockmodel.KStockModel()


#股票列表
def basic_data():
    basic = ts.get_stock_basics()
    # data = json.loads(basic_data.to_json(orient='records'))
    for i in basic.index:
        item = basic.ix[i].to_dict()
        item['code'] = i
        item['timeToMarket'] = float(item['timeToMarket'])
        item['holders'] = float(item['holders'])
        basic_model.replace_one(item, code=i)


def k_stock():
    stock_list = basic_model.find()
    for stock in stock_list:
        print(stock['code'])
        k = ts.get_k_data(stock['code'])
        if len(k) > 0:

            data = json.loads(k.to_json(orient='records'))
            k_model.insert(data)


def per_day_task():
    basic_data()





def done(e):
    print('done')

k_stock()

#scheduler.add_job(per_day_task, 'cron', hour='6')
#scheduler.add_listener(done, events.EVENT_JOB_EXECUTED)
#cheduler.start()


# 每天6点 爬取盘面数据
# 股票列表
# 股票行情
