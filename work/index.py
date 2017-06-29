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


class Qsm(Crawler):
    def __init__(self):
        self.headers = {

        }
