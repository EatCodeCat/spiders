import tushare as ts
import json
from mongodao import stockmodel


def basic_data():
    basic_data = ts.get_stock_basics()
    data = json.loads(basic_data.to_json(orient='records'))
    stockmodel.BasicStockModel().insert(data)

basic_data()

#每天6点 爬取盘面数据
#股票列表
#股票行情

