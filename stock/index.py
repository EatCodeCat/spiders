import json
import tushare as ts
from mongodao import stockmodel
from stock.mongodbscheduler import scheduler


def basic_data():
    basic = ts.get_stock_basics()
#    data = json.loads(basic_data.to_json(orient='records'))
    for i in basic.index:
        item = basic.ix[i]
        item['code'] = i;
        print (item)
#    stockmodel.BasicStockModel().replace_one(data)


def per_day_task():
    basic_data()


#scheduler.add_job(basic_data, 'cron', day_of_week="0-4", hour=18)

basic_data()

# 每天6点 爬取盘面数据
# 股票列表
# 股票行情
