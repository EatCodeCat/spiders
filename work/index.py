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



import sys

sys.path.append("..")

from minspider.webspider import WebSpider
import datetime
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler
import sqlite3
from flask import Flask, g, jsonify, render_template, request, make_response
import re

touzhuInfo_list = [{
    'keyword': '財布',  # 关键字
    'gd_no_list': ['524152697'],  # 投注id
    'inc': 50
}]

# usename = 'flower_424'  # 用户名称

usename = 'ameng1120'  # 用户名称
cust_no = '240721731'

userinfo = {
    'username': 'username',
    'cookie': ''
}

pwd = ''  # 密码
execHour = ''  # 执行时点
execMins = ''  # 执行分钟


def do_touzhu(item):
    result_list = []
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
        'cookie': 'inflow_referer=direct; tracking-devcd-7=Windows_NT_10.0%3a%3aChrome%3a%3aDesktop; tracking-landing-page=0!%3a%3a!; tracking-sessionid=23e4d83f-b419-43a2-9a8d-2a2158bc13fc::2017-07-01 15:10:55; Language=zh-CN; ck_login_sc=Y; ASP.NET_SessionId=mur5cj33pwntjozpiyuth5e2; GiosisGsmJP=A7351A0E9BE35408AA6D5716C666FB6C033FF8A673B49E267BC6BA259FD3CE990A6FF856BCAAD9D34B76B2F6694087E9744582184870434AFEC50EACAEDDB283AAB8B01433F99EAEA665FF03E4AF11807D545798E381D95C0D20DBD5686BFB068035A64C6F7C7A3590C1FD82FA3B16FD3AD3ACFF383D4D4B0C42ABBD28AFC513FA2717B7B0260FB20B22F4744BCA1850604852C38908FDED96D13DFCC88626B3334A1DAD0EA453A1B063B218C79A5401CBDDEFF13ABF5157F244DEF6004470285E506206B24720F5EDCE0393140BF6D3658DE21B53DF71BE4536826247781747470106A8DC39E2D2F96817C23F62734694331EC85E25C4A232D42CA1396DF7146525C04C20C1CE71F42E4CAD366E6BE41535ABB7525C2FA947B03D4B233F982C4B81F5800570A440AA46BC1A018CD20AB7BD39EEE0CA11C39963FC789D2BCF23301D9E51F423171D35D57B43E34352F2864267DD; ID_SAVE=LrT3kB08auQ=; LANG_SAVE=zh-cn; qsm_cust_no=240721731; seller_reg_dt=2015-08-31+11%3a06%3a43; qstore_type=Basic; qstore_status=Approved; APPLY_CONFM_YN=Y; C_SVC_NATIONS=JP%7cUS%7c; IsOriginSvcNation=Y; OriginSvcNation=JP; EP_NO=; ck_outer_items_set=N'
    })

    html = wsp.get_text('http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/ADPlus/ADPlusKeyword.aspx')

    m = re.search(r'"cust_no"\s*:\s*"(\d+)"', html)
    if m is not None:
        cust_no = m.group(1)

    # 获取投注第一行金额
    fetch_top_price_url = 'http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/GetPlusItemKeywordGroup'

    params = {"keyword": item['keyword'], "plus_type": "KW", "___cache_expire___": str(datetime.datetime.now())}

    text = wsp.post(fetch_top_price_url, data=json.dumps(params)).json()
    org_plus_id = text['d']['org_plus_id']
    if len(text['d']['KW']['list_bid']) > 0:
        price = text['d']['KW']['list_bid'][0]['bid_price']
    else:
        result_list.append({
            'touzhuresult': '关键字没有投注金额'
        })
        return result_list

    # 投注
    inc = item['inc']
    bid_price_list = int(price) + inc

    for id in item['gd_no_list']:
        post = {"org_plus_id_list": org_plus_id, "cust_no": cust_no, "user_id": usename, "gd_no": id,
                "sid": id, "bid_price_list": bid_price_list,
                "bid_start_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "bid_end_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "landing_type": "", "landing_url": "", "img_url": "", "remark": "", "display_type": "B",
                "___cache_expire___": str(datetime.datetime.now())}
        result = wsp.post('http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/PlaceBidKeyword',
                          data=json.dumps(post)).json()

        r_result = {'top_price': price, 'inc': inc, 'bid_price_list': bid_price_list, 'id': id}
        if result['d']['ResultCode'] == 0:
            r_result['touzhuresult'] = '投注成功'
        else:
            r_result['touzhuresult'] = '投注失败-' + result['d']['ResultMsg']
        result_list.append(r_result)

    # {__type: "GMKT.INC.Framework.Core.StdResult", ResultCode: 0, ResultMsg: "SUCCESS"}
    return result_list


app = Flask(__name__, static_folder='dist', template_folder='dist')


def do_touzhuInfo_list(keyword, gd_no_list, id):
    app.logger.info('开始任务key:%s, gd_no_list:%s, id:%s', keyword, gd_no_list, id)
    try:
        result = do_touzhu({
            'keyword': keyword,  # 关键字
            'gd_no_list': gd_no_list.split(','),  # 投注id
            'inc': 50
        })
        con = sqlite3.connect('qsm.db')
        cur = con.cursor()
        cur.execute('update task set result=?, exec_time=? where id=' + str(id), [str(json.dumps(result)),
                                                                                  datetime.datetime.now().strftime(
                                                                                      '%Y-%m-%d %H:%M:%S')])
        con.commit()
        con.close()

    except Exception as e:
        app.logger.exception('异常任务', e)


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


def execute_sql(sql, *arg):
    con = get_db()
    cur = con.cursor()
    cur.execute(sql, arg)
    con.commit()


def fetch_one(sql, *arg):
    con = get_db()
    cur = con.cursor()
    cur.execute(sql, arg)
    return cur.fetchone()


@app.route('/api/pause/<id>')
def scheduler_pause(id):
    execute_sql('update task set status=1 where id=?', id)

    job_id = 'task_' + id
    job = scheduler.get_job(job_id)
    if job is None:
        add_job(job_id)
    else:
        scheduler.pause_job(job_id)
    return 'pause!'


@app.route('/api/resume/<id>')
def scheduler_resume(id):
    execute_sql('update task set status=0 where id=?', id)
    job_id = 'task_' + id
    job = scheduler.get_job(job_id)
    if job is None:
        add_job(id)
    else:
        scheduler.resume_job(job_id)
    return 'resume'


@app.route('/api/remove/<id>')
def scheduler_remove(id):
    execute_sql('delete from task where id=?', id)
    job_id = 'task_' + id
    job = scheduler.get_job(job_id)
    if job is not None:
        scheduler.delete_job(job_id)
    return jsonify(result=0)


@app.route('/api/list')
def list():
    cur = get_db().cursor()
    cursor = cur.execute('select * from task')
    all = cursor.fetchall()
    return jsonify(all)


@app.route('/api/add/<name>/<key>/<idlist>')
def add_scheduler(name, key, idlist):
    # status 0 等待执行， 1 暂停, 2 停止
    arg = [name, '', key, idlist, '0', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    execute_sql('insert into task (name, result, key,gn_id_list, status, exec_time) values (?,?,?,?,?,?)', *arg)
    cur = get_db().cursor()
    cursor = cur.execute('select max(id) from task')
    id = cursor.fetchone()[0]
    add_job(id)
    return jsonify(result=0)


def add_job(task_id):
    job = scheduler.get_job(task_id)
    if job is None:
        task = fetch_one('select * from task where id=' + str(task_id))
        task = [task[1], task[4], task[0]]
        scheduler.add_job('task_' + str(task_id), do_touzhuInfo_list, trigger='cron', hour=15-8, minute=40, args=task)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def hello(*args, **kwg):
    print("hello")


con = sqlite3.connect('qsm.db')
cur = con.cursor()
cur.execute('update task set status=2')
con.commit()
con.close()
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
