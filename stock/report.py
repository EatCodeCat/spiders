# coding=utf-8
__author__ = 'think'

import pandas
from pandas import Series, DataFrame
from mongodao import stockmodel

basic_model = stockmodel.BasicStockModel()
k_model = stockmodel.KStockModel()

k = k_model.find(code='600000')

stock_list = []
columns = []
for stock in k:
    columns = stock.keys()
    stock_list.append(stock.values())

df = DataFrame(stock_list, index=['code'], columns=columns)
min(df['close'])
