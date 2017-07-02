import sys

sys.path.append("..")

from minspider.webspider import WebSpider
import datetime
import json
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

log_file = 'server.log'
error_log = 'error.log'


def log_info(msg: str, *args):
    try:
        with open(log_file, 'a') as f:
            f.writelines(now_time_str() + '--' + (msg % args) + '\r\n')
    except:
        pass


def log_error(msg: str, *args):
    try:
        with open(error_log, 'a') as f:
            f.writelines(now_time_str() + '--' + (msg % args) + '\r\n')
    except:
        pass


def do_touzhu(item):
    log_info('查询关键字--key:%s', item['keyword'])

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
        log_info('关键字没有投注金额--end')
        result_list.append({
            'touzhuresult': '关键字没有投注金额'
        })
        return result_list

    log_info('获取投注第一行金额--price:%s', price)
    # 投注
    inc = item['inc']
    bid_price_list = int(price) + inc

    for gid in item['gd_no_list']:
        log_info('开始投注ID--:%s', gid)
        post = {"org_plus_id_list": org_plus_id, "cust_no": cust_no, "user_id": usename, "gd_no": gid,
                "sid": gid, "bid_price_list": bid_price_list,
                "bid_start_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "bid_end_dt": str(datetime.datetime.today().strftime('%Y-%m-%d')),
                "landing_type": "", "landing_url": "", "img_url": "", "remark": "", "display_type": "B",
                "___cache_expire___": str(datetime.datetime.now())}
        post_params = json.dumps(post)
        result = wsp.post('http://qsm.qoo10.jp/GMKT.INC.Gsm.Web/swe_ADPlusBizService.asmx/PlaceBidKeyword',
                          data=post_params).json()
        r_result = {'top_price': price, 'inc': inc, 'bid_price_list': bid_price_list, 'id': gid}
        if result['d']['ResultCode'] == 0:
            r_result['touzhuresult'] = str(gid) + '投注成功'
        else:
            r_result['touzhuresult'] = str(gid) + '投注失败-' + result['d']['ResultMsg']
        result_list.append(r_result)
        log_info('投注结果--:%s', str(result))

    # {__type: "GMKT.INC.Framework.Core.StdResult", ResultCode: 0, ResultMsg: "SUCCESS"}
    return result_list


import logging

# from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__, static_folder='dist', template_folder='dist')


# server_log = TimedRotatingFileHandler('server.log', 'D')
# server_log.setLevel(logging.DEBUG)
# server_log.setFormatter(logging.Formatter(
#     '%(asctime)s %(levelname)s: %(message)s\r\n'
# ))
#
# error_log = TimedRotatingFileHandler('error.log', 'D')
# error_log.setLevel(logging.ERROR)
# error_log.setFormatter(logging.Formatter(
#     '%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d]\r\n'
# ))
#
# app.logger.addHandler(server_log)
# app.logger.addHandler(error_log)


def do_touzhuInfo_list(keyword, gd_no_list, _id):
    log_info('开始任务--key:%s, gd_no_list:%s, id:%s', keyword, gd_no_list, _id)
    con = sqlite3.connect('qsm.db')
    cur = con.cursor()
    try:
        result = do_touzhu({
            'keyword': keyword,  # 关键字
            'gd_no_list': gd_no_list.split(','),  # 投注id
            'inc': 50
        })
        cur.execute('update task set result=?, exec_time=? where id=' + str(_id), [json.dumps(result), now_time_str()])
    except Exception as e:
        cur.execute('update task set result=?, exec_time=? where id=' + str(_id),
                    [json.dump({'touzhuresult': '任务异常' + str(e)}), now_time_str()])
        log_error('异常任务', e)
    con.commit()
    con.close()


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


def now_time_str():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def test_task(*args):
    print(args)


def add_job(task_id):
    job = scheduler.get_job("task_" + str(task_id))
    if job is None:
        task = fetch_one('select * from task where id=' + str(task_id))
        args = [task[3], task[4], task[0]]
        scheduler.add_job('task_' + str(task_id), do_touzhuInfo_list, trigger='cron', hour=task[8], minute=task[9],
                          second=task[10], args=args)


@app.route('/api/pause/<_id>')
def scheduler_pause(_id):
    job_id = 'task_' + _id
    job = scheduler.get_job(job_id)
    if job is not None:
        scheduler.pause_job(job_id)
    execute_sql('update task set status=1 where id=?', _id)
    return 'pause!'


@app.route('/api/resume/<_id>')
def scheduler_resume(_id):
    job_id = 'task_' + _id
    job = scheduler.get_job(job_id)
    if job is None:
        add_job(_id)
    else:
        scheduler.resume_job(job_id)
    execute_sql('update task set status=0 where id=?', _id)
    return 'resume'


@app.route('/api/remove/<_id>')
def scheduler_remove(_id):
    job_id = 'task_' + _id
    job = scheduler.get_job(job_id)
    if job is not None:
        scheduler.delete_job(job_id)
    execute_sql('delete from task where id=?', _id)
    return jsonify(result=0)


@app.route('/api/list')
def list():
    cur = get_db().cursor()
    cursor = cur.execute('select * from task order by id desc')
    all = cursor.fetchall()
    return jsonify(all)


@app.route('/api/add/<name>/<key>/<idlist>/<h>/<m>/<s>')
def add_scheduler(name: str, key: str, idlist, h, m, s):
    # status 0 等待执行， 1 暂停, 2 停止
    arg = [name.strip(), key.strip(), idlist.strip(), '0', h, m, s]
    execute_sql('insert into task (name, key,gn_id_list, status, h, m, s) values (?,?,?,?,?,?,?)', *arg)
    cur = get_db().cursor()
    cursor = cur.execute('select max(id) from task')
    id = cursor.fetchone()[0]
    add_job(id)
    log_info('添加一个任务--key:%s, gd_no_list:%s,status:%s, id:%s, time=%s:%s:%s', *arg)
    return jsonify(result=0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/time')
def time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.route('/log_sever')
def log():
    f = open('server.log', 'r')
    str = []
    while True:
        line = f.readline()
        str.append(line)
        if len(line) == 0:  # Zero length indicates EOF
            break
    f.close()
    return '<br/>'.join(str)


@app.route('/log_error')
def error_log():
    f = open('error.log', 'r')
    str = []
    while True:
        line = f.readline()
        str.append(line)
        if len(line) == 0:  # Zero length indicates EOF
            break
    f.close()
    return '<br/>'.join(str)


con = sqlite3.connect('qsm.db')
cur = con.cursor()
cur.execute('update task set status=2')
con.commit()
con.close()
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        app.debug = True
    try:
        app.run(host='0.0.0.0')
    except Exception as e:
        log_error('app异常任务', e)
