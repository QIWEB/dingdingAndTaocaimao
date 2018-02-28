#!/usr/bin/python
# -*- coding: utf-8 -*-

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import json

# 登录的主页面
hosturl = 'http://123.103.9.117:9001' # 自己填写
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'http://123.103.9.117:9001/service/login' # 从数据包中分析出，处理post请求的url

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
#cj = cookielib.LWPCookieJar()
#cookie_support = urllib2.HTTPCookieProcessor(cj)
#opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#urllib2.install_opener(opener)

# 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
#h = urllib2.urlopen(hosturl)

# 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/6.6.17)'
  # , 'Referer': 'hosturl'
           }
postData = {'password': 'dmlogin'}

userid=None
sessionkey=None
# 构造Post数据，他也是从抓大的包里分析得出的。
'''
postData = {'password': 'dmlogin',
            'f': 'st',
            'user': '******', // 你的用户名
'pass': '******', // 你的密码，密码可能是明文传输也可能是密文，如果是密文需要调用相应的加密算法加密
'rmbr': 'true', // 特有数据，不同网站可能不同
'tmp': '0.7306424454308195' // 特有数据，不同网站可能不同
'password': 'YTExMTExMTE%3D%0A',
             YTExMTExMTE%3D%0A
'''
#提交post
def do_post(posturl,postData):
    request = urllib2.Request(posturl, postData, headers)
    print request
    response = urllib2.urlopen(request)
    text = response.read()

    return text


#postData = urllib.urlencode(postData)

#----------------------------------------------登录----------------------
# 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
# 需要给Post数据编码

def do_login():

    postData = {
        'usercode': 'caohailong1',
        'password': 'YTExMTExMTE%3D%0A'

    }
    postData = 'password=YTExMTExMTE%3D%0A&usercode=xinghla'#caohailong1 和xinghla
    text=do_post(posturl,postData)
    return text







#postData='password=YTExMTExMTE%3D%0A&usercode=caohailong1'




#-----------------------------------------------签到--------------------------

#postData = urllib.urlencode(postData)
def sign(txt,workdate):

    posturl = 'http://123.103.9.117:9001/service/submitMyWorkRecord'
    postData = {
        'task_desc': '交银金融租赁2016年度LAS和LQS业务系统技术开发的项目(租赁事业部)',
        'imei': '99000764107289',
        'projectstatus': '驻场运维阶段',
        'deviceversion': '手机型号:Redmi 3  android系统:5.1.1app版本号:1.8.0.6',
        'workdesc': '签到',
        'phone': '',
        'gprsinfo': '中国上海市浦东新区银城中路501号-临',
        'projectid': '1001AZ1000000000SOZG',
        'workdate': workdate,
        'sessionkey':sessionkey,#dictinfo["sessionkey"],
        'userid':userid#dictinfo["userid"]
    }
    postData = urllib.urlencode(postData)
    print postData
    text = do_post(posturl, postData)#提交

#-----------------------------------------------查询日志--------------------------
def getMyWorkRecord(pageid):
    posturl = 'http://123.103.9.117:9001/service/getMyWorkRecord'
    postData = {'sessionkey':sessionkey,
                'userid':userid,
                'pageindex':pageid
        #,
               # 'gprsinfo': '中国上海市浦东新区银城中路501号-临'
                }
    postData = urllib.urlencode(postData)
    #postData='sessionkey = '+sessionkey+' & pageindex = 1 & userid = 1001AZ1000000000RHXD &'
    text1 = do_post(posturl, postData)
    return text1


text=do_login()
print '登录成功'
dictinfo = json.loads(text)
userid=dictinfo["userid"]
sessionkey=dictinfo["sessionkey"]



#查询
def do_query():
    pageid = raw_input('please input a pageNo:\n')
    v1=getMyWorkRecord(pageid)
    print v1
    dictinfo1 = json.loads(v1)
    #得到日志vo
    dictinfo2 = dictinfo1["worklst"]

    for vo in dictinfo2:
        print vo["rn"]+"___"+vo['user_name']+"___"+vo['workdate']+"___"+vo['workdesc']+"___"+vo['dmydate']+"___"+vo['projectname']+"___"+vo['gprsinfo']
    do_query()



workdate='2016-06-20 17:57:38'
sign(text,workdate)
print '签到成功'
do_query()
'''
POST http://123.103.9.117:9001/service/login HTTP/1.1
If-Modified-Since: Mon, 20 Jun 2016 04:39:00 GMT+00:00
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/6.6.17)
Host: 123.103.9.117:9001
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 48

password=YTExMTExMTE%3D%0A&usercode=caohailong1&
登录
返回
{"sessionkey":"YFWJYNRYPFYYEYJRRNNPPYWKGGRYYGEO","username":"曹海龙\n","returncode":"0","userid":"1001AZ1000000000RHXD","isprojectrole":"1","isprojectmanager":"1","ismanager":"0","msg":"登录成功","workgrouplist":[{"name":"租赁事业部","pk_workgroup":"1001AZ1000000000RDIU"}]}

成功之后首页
POST http://123.103.9.117:9001/service/queryApplyCountServlet HTTP/1.1
If-Modified-Since: Mon, 20 Jun 2016 04:42:02 GMT+00:00
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/6.6.17)
Host: 123.103.9.117:9001
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 72

sessionkey=YFWJYNRYPFYYEYJRRNNPPYWKGGRYYGEO&userid=1001AZ1000000000RHXD&

返回
{"approvecount":"1","returncode":"0","recordcount":"0","msg":"成功"}



POST http://123.103.9.117:9001/service/queryApplyCountServlet HTTP/1.1
If-Modified-Since: Mon, 20 Jun 2016 04:40:29 GMT+00:00
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/6.6.17)
Host: 123.103.9.117:9001
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 72

sessionkey=YFWJYNRYPFYYEYJRRNNPPYWKGGRYYGEO&userid=1001AZ1000000000RHXD&
注销
返回
{"approvecount":"1","returncode":"0","recordcount":"0","msg":"成功"}


查看项目
POST http://123.103.9.117:9001/service/getApplyMsg HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/6.6.17)
Host: 123.103.9.117:9001
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 85

versionno=-1&sessionkey=YFWJYNRYPFYYEYJRRNNPPYWKGGRYYGEO&userid=1001AZ1000000000RHXD&



{"projectlst":[{"name":"交银金融租赁2014年度LAS和LQS业务系统技术","pk_product":"1001AZ1000000000RZWL"},{"name":"交银金融租赁2015年度LAS和LQS业务系统技术开发项目","pk_product":"1001AZ1000000000SNLU"},{"name":"交银金融租赁银企直连项目","pk_product":"1001AZ1000000000SNLV"},{"name":"交银金融租赁2016年度LAS和LQS业务系统技术开发的项目","pk_product":"1001AZ1000000000SOZG"}],"supportlst":[{"supportname":"售前","supportid":"SUP00000001"},{"supportname":"实施","supportid":"SUP00000002"},{"supportname":"需求\/方案","supportid":"SUP00000003"},{"supportname":"支持服务","supportid":"SUP00000004"},{"supportname":"培训","supportid":"SUP00000005"}],"arealst":[{"name":"华北银行ABU","pk_area":"1001AZ1000000000KX8D"},{"name":"华南证券综合ABU","pk_area":"1001AZ1000000000KX9N"},{"name":"北方证券综合ABU","pk_area":"1001AZ1000000000KXAX"},{"name":"华南银行ABU","pk_area":"1001AZ1000000000KXAZ"},{"name":"北方银行ABU","pk_area":"1001AZ1000000000KXB1"},{"name":"华东银行ABU","pk_area":"1001AZ1000000000KXB5"},{"name":"华东证券综合ABU","pk_area":"1001AZ1000000000KXFH"},{"name":"租赁事业部","pk_area":"1001AZ1000000000RDIU"},{"name":"保险信托事业部-南方销售部","pk_area":"1001AZ1000000000R4Y4"},{"name":"保险信托事业部-北方销售部","pk_area":"1001AZ1000000000R4Y9"},{"name":"北方非银服务ABU","pk_area":"1001AZ1000000000RZ67"},{"name":"保险与信托事业部-交付中心北方实施","pk_area":"1001AZ1000000000SLNA"},{"name":"西南ABU开发组","pk_area":"1001AZ1000000000O1ZJ"},{"name":"西南ABU实施组","pk_area":"1001AZ1000000000O1ZS"},{"name":"西南ABU常务组","pk_area":"1001AZ1000000000O20A"},{"name":"西南ABU销售组","pk_area":"1001AZ1000000000O21N"}],"returncode":"0","deptlst":[{"name":"ERP事业部_解决方案部","pk_workgroup":"1001AZ1000000000KVT4"},{"name":"金融互联网业务系统平台","pk_workgroup":"1001AZ1000000000LQG2"},{"name":"保险与信托事业部-交付中心北方实施","pk_workgroup":"1001AZ1000000000SLNA"},{"name":"市场与业务拓展部","pk_workgroup":"1001AZ1000000000SMD8"},{"name":"项目管理部","pk_workgroup":"1001AZ1000000000SMDJ"},{"name":"ERP事业部_咨询实施部","pk_workgroup":"1001AZ1000000000RS5J"}],"msg":"成功"}
'''

print '测试:',len("YTExMTExMTE%3D%0A")