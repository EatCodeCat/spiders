# http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/GetBiddingList
# {"cust_no":"243841656","plus_type":"KG","bid_stat":"S3","srch_option":"O","srch_value":"","bid_start_dt":"2017-06-28","bid_end_dt":"2017-06-28","___cache_expire___":"Thu Jun 29 2017 14:44:55 GMT+0800 (中国标准时间)"}




# http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/GetPlusItemKeywordGroup

# {"keyword":"財布","plus_type":"KW","___cache_expire___":"Thu Jun 29 2017 14:14:25 GMT+0800 (中国标准时间)"}



'''
POST /GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/GetPlusItemKeywordGroup HTTP/1.1
Host: qsm.qoo10.jp
Connection: keep-alive
Content-Length: 115
Origin: http://qsm.qoo10.jp
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Content-Type: application/json
Accept: */*
Referer: http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/ADPlus/ADPlusKeyword.aspx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,nb;q=0.2,sk;q=0.2,zh-TW;q=0.2
Cookie: inflow_referer=direct; tracking-devcd-7=Windows_NT_6.1%3a%3aChrome%3a%3aDesktop; ASP.NET_SessionId=41ypvw1rkowfuseelmxbae11; tracking-landing-page=0!%3a%3a!; tracking-sessionid=43d9cefc-0c1f-4996-9c42-580ead695ead::2017-06-29 14:31:05; Language=zh-CN; GiosisGsmJP=EC9427520D49649641193698B3D63504AA32D989573EF13A2AD8613741233BB5CE73F98BE44D284B3529DCEB72189E564E2C64B87F1DB6BAA1FAF04AB0AAB3EDF7C07485CE323D8230647864F3F2379B426852F588F472342379FB46D3BC0B3992807B1903696102332E6335A14186A5CD58E79AEB61BDF5A76D04FE712B8EA2EB694145975210BCB0C8C17AFC7196144D71C62C73ECE5CD462F38D62DF7055A160E32514B842345BABC8E8F5CD957FEACEBF161E4C33DB15E10F8F80CC81321E91BA1C9FFA9599F5757E9FD00FACCA6475FFE7C6B4675218E5C3787818D916778677C3BA4737BEC088D70D4383E9F0ACC1C70C92789CB8ACFB7A4ABA7849A9B84460A290D447A380A626D390DD869FBB2A718249C4C94FC528F76757A50FB07C9D5B8AE8E2D659750DEB7A8293852AB39E3E0B651F488409FC5001E5641E78A40A9C54AB6EA5BC5678A4D70C9DD2B08CE857D6C; ID_SAVE=LrT3kB08auQ=; qsm_cust_no=243841656; seller_reg_dt=2016-11-01+14%3a11%3a20; qstore_type=; qstore_status=; APPLY_CONFM_YN=Y; C_SVC_NATIONS=JP%7c; IsOriginSvcNation=Y; OriginSvcNation=JP; EP_NO=; ck_login_sc=Y; ck_outer_items_set=N; LANG_SAVE=zh-cn
'''

# http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_GSMSearchBizService.asmx/ADPlusSearchGoodsList

# {"plus_type":"KW","keyword":"524152697","pageSize":"100","group_code":"","gdlc_cd":"","gdmc_cd":"","gdsc_cd":"","sell_login_id":"flower_424","___cache_expire___":"Thu Jun 29 2017 14:23:18 GMT+0800 (中国标准时间)"}




# http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/PlaceBidKeyword

# {"org_plus_id_list":"453","cust_no":"243841656","user_id":"flower_424","gd_no":"524152697","sid":"524152697","bid_price_list":"500","bid_start_dt":"2017-06-29","bid_end_dt":"2017-06-29","landing_type":"","landing_url":"","img_url":"","remark":"","display_type":"B","___cache_expire___":"Thu Jun 29 2017 14:24:30 GMT+0800 (中国标准时间)"}



from  minspider.crawler import Crawler

from minspider.webspider import WebSpider

import datetime
import json

touzhuInfo_list = [{
    'keyword': '財布',  # 关键字
    'gd_no_list': ['524152697'],  # 投注id
    'inc': 50
}]

usename = 'flower_424'  # 用户名称

pwd = ''  # 密码
execHour = ''  # 执行时点
execMins = ''  # 执行分钟


def do_touzhu(item):
    wsp = WebSpider({
        'host': 'qsm.qoo10.jp',
        'connection': 'keep-alive',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,nb;q=0.2,sk;q=0.2,zh-TW;q=0.2',
        'cookie': 'tracking-sessionid=43d9cefc-0c1f-4996-9c42-580ead695ead::2017-06-29 14:31:05; inflow_referer=direct; tracking-devcd-7=Windows_NT_6.1%3a%3aChrome%3a%3aDesktop; tracking-landing-page=0!%3a%3a!; ASP.NET_SessionId=wjgdopnktimrx3122gybebw1; Language=zh-CN; GiosisGsmJP=8BA34F267521110DE071313FC07CCF6A4BD354F475FA5CF66644B3F4843E59D033A6F9079B41174935C2FDD3D7171D63245B018B180A5591059D4026C26FA890BED63D4A74E76288CAB039BB408BE7BEA15116F52ED62DE3A9A3A474ED46720BB376405942D41BF1F874BF43BD90B4C056E3079C4925053F9E6AFCA21241A21AA2392738044786AD9352E14FBD62C0FF144EA148F319AF033D0AADAC34C6E7EA85ACE178EC028C3C388930667F0507DEC594DFAF524CC4963A3B62A5B3DD409DC5AC8CDBF16FD6973F9C1D4A9737A6222ACF1D2768F81D2450431FE1B3CBC4A9E60B4E5DE3EAE9C9DE720334D43E4A4A852D60D10EA569123CF94539F6C9AD5AE48D800A84ECE9BA6D77D3F24849226BD33525D7B2D0609AFFC4E4990A64B3ECCCA570FCBA5E252D30CBDE7EA64431BDB5D4D7EC699BA4D28412DA3E29CE13497170B9A61F1DA7F9594F6B0B498B4C49FA28D832; ID_SAVE=LrT3kB08auQ=; LANG_SAVE=zh-cn; ck_outer_items_set=; qsm_cust_no=243841656; seller_reg_dt=2016-11-01+14%3a11%3a20; qstore_type=; qstore_status=; APPLY_CONFM_YN=Y; C_SVC_NATIONS=JP%7c; IsOriginSvcNation=Y; OriginSvcNation=JP; EP_NO='
    })

    # 获取投注第一行金额
    fetch_top_price_url = 'http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/GetPlusItemKeywordGroup'

    params = {"keyword": item['keyword'], "plus_type": "KW", "___cache_expire___": str(datetime.datetime.now())}

    text = wsp.post(fetch_top_price_url, data=json.dumps(params)).json()
    price = text['d']['KW']['list_bid'][0]['bid_price']
    # 投注
    inc = item['inc']
    bid_price_list = int(price) + inc

    result_list = {}
    for id in item['gd_no_list']:
        post = {"org_plus_id_list": "453", "cust_no": "243841656", "user_id": usename, "gd_no": id,
                "sid": id, "bid_price_list": bid_price_list,
                "bid_start_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "bid_end_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "landing_type": "", "landing_url": "", "img_url": "", "remark": "", "display_type": "B",
                "___cache_expire___": str(datetime.datetime.now())}
        result = wsp.post('http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/PlaceBidKeyword',
                          data=json.dumps(post)).json()
        result_list[id] = {'touzhuresult:': result, 'top_price': price, 'inc': inc, 'bid_price_list': bid_price_list}

    # {__type: "GMKT.INC.Framework.Core.StdResult", ResultCode: 0, ResultMsg: "SUCCESS"}
    print(result_list)
    return result_list


def do_touzhuInfo_list():
    touzhuInfo_list = touzhuInfo_list = [{
        'keyword': '財布',  # 关键字
        'gd_no_list': ['524152697'],  # 投注id
        'inc': 50
    }]
    for item in touzhuInfo_list:
        do_touzhu(item)


from flask import Flask
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler
import sqlite3
from flask import g

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('qsm.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/pause')
def scheduler_pause():
    print(scheduler.get_jobs())
    scheduler.pause_job('hello')
    return 'pause!'


@app.route('/resume')
def scheduler_resume():
    scheduler.resume_job('hello')
    return 'resume'


@app.route('/remove')
def scheduler_remove():
    scheduler.delete_job('hello')
    return 'remove'


@app.route('/add')
def add_scheduler():
    cur = get_db().cursor()
    # status 0 正在执行， 1 暂停  2 停止
    arg = ['財布', '', '財布', '524152697', '0', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    cur.execute('insert into task (name, result, key,gn_id_list, status, exec_time) values (?,?,?,?,?,?)', arg)
    scheduler.add_job('hello', hello, trigger='interval', seconds=3)
    return 'Hello World!！！！！！'


def hello():
    print('hello')


if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.debug = True
    app.run()
