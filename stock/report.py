# coding=utf-8
__author__ = 'think'

import pandas
from pandas import Series, DataFrame
from mongodao import stockmodel
from collections import OrderedDict

basic_model = stockmodel.BasicStockModel()
k_model = stockmodel.KStockModel()

# maxlist = k_model.aggregate([
#     {
#         '$match': {'date': {'$gt': '2017-04-01'}}
#     },
#     {
#         '$group':
#             {
#                 '_id': "$code",
#                 'close': {'$max': "$close"}
#             },
#     }
# ])

maxlist = k_model.find({'date': '2017-07-07'})

minlist = k_model.aggregate([{
    '$match': {'date': {'$gt': '2017-04-01'}}}
    , {
        '$group':
            {
                '_id': "$code",
                'close': {'$min': "$close"}
            },
    }
])

stock_dict = {}
columns = []
for stock in maxlist:
    val = stock['close']
    stock_dict[stock['code']] = {'max': val}

stock_list = basic_model.find()
stock_dict2 = {item['code']: item for item in stock_list if float(item['timeToMarket']) < 20170101}

with open('20170401-20170707.csv', 'w') as f:
    f.write('code,name,industry,min,max,m_growth\n');
    for stock in minlist:
        code = stock['_id']
        if code in stock_dict and code in stock_dict2:
            val = stock['close']
            stock_dict[code]['min'] = val
            max_p = stock_dict[code]['max']
            m_growth = ((max_p - val) / val) * 100
            f.writelines('{0},{1},{2},{3},{4},{5}%\n'.format(code, stock_dict2[code]['name'],stock_dict2[code]['industry'], val, max_p, m_growth))

print('done')
