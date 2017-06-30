import sqlite3
import datetime


def food(*args):
    print(args)

if __name__ == '__main__':
    con = sqlite3.connect('qsm.db')
    cur = con.cursor()
    cur.execute('update task set result=?,exec_time=? where id=3',["{'524152697': {'touzhuresult:': {'d': {'__type': 'GMKT.INC.Framework.Core.StdResult', 'ResultCode': -21, 'ResultMsg': 'FAIL[-21]'}}, 'top_price': 650.0, 'inc': 50, 'bid_price_list': 700}}"
        ,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
                )
    con.commit()
    con.close()
