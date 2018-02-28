#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form fd request
#
# Created: 2016年6月21日13:21:35
#      by: qiweb
#
# WARNING! All changes made in this file will be lost!
import urllib
import urllib2
import cookielib
import json
import time
import random
import os

class qiwebTaoCaiMao:
    USER_NAME=["15889723562","13671571294","13002645604","13184394616"]
    PASSWROD=["123456","123456","123456","123456"]
    user_index=0
    Host="http://m.taocaimall.com"
    cookievalue=None
    user_now=None

    appLongoutUrl="http://m.taocaimall.com/taocaimall/appLongout.json"
    appLongin1="https://m.taocaimall.com/taocaimall/appLongin.json"
    #{"op_flag":"success","info":"登录成功","sessionid":"8CCFE649B3044EC927EF08B5CC567466","addrInfo":{"areaInfo":"6号楼201","trueName":"张七","areas":[{"level":"3","areaName":"锦博苑","areaId":"4534030"},{"level":"2","areaName":"浦东新区","areaId":"4522861"},{"level":"1","areaName":"上海市","areaId":"4522848"},{"level":"0","areaName":"上海市","areaId":"4522847"}],"lng":"121.542458","addr_id":"44019","telephone":"15889723562","lat":"31.194206"},"userId":"76447"}

    appLongin2="http://m.taocaimall.com/taocaimall/saveClientId.json"
    appLongin3="http://m.taocaimall.com/taocaimall/buyer/getRongCloudToken.json"

    discountCouponUrl="http://m.taocaimall.com/taocaimall/buyer/list_discountCoupon_1.json"
    User_Agent="okhttp/2.4.0"#Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36"
    rongCloudToken=None
    JSESSIONID=None
    sessionid=None
    userId=None
    addrInfo=None
    telephone=None

    #------------------------------------do_get_post------------------------------------
    def do_get_post(self,url,postdata):
        text = None
        try:
            req = urllib2.Request(url,
                                  postdata)  # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.


            req.add_header('User-Agent', self.User_Agent)
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Cache-Control', 'no-cache')
            req.add_header('Cookie', self.cookievalue)
            req.add_header('Accept', '*/*')
            req.add_header('Connection', 'Keep-Alive')
            resp = urllib2.urlopen(req)
            if(url.find("appLongin.json")!=-1):#判断为登录获取cookie
                setcookie=resp.headers.headers[7]
                index=setcookie.find("JSESSIONID")
                self.cookievalue=setcookie[index:index+43]
            text = resp.read()

            if (url.find("viewSignin.htm") == -1):  # 判断为查看积分
                print text
        except Exception:
            print '哎呀，请求又超时了！'
        #respInfo = resp.info()
        # print respInfo

        return text

    # ------------------------------------do_get_post_html------------------------------------
    #目前还没使用此函数
    def do_get_post_html(self, url, postdata):
        self.User_Agent="Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36"
        req = urllib2.Request(url,
                              postdata)  # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.

        req.add_header('User-Agent', self.User_Agent)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Accept', '*/*')
        req.add_header('Connection', 'Keep-Alive')
        resp = urllib2.urlopen(req)
        # respInfo = resp.info()
        # print respInfo
        text = resp.read()
        print text
        return text

    #------------------------------------登录------------------------------------
    def login(self,username,password):
        self.user_now=username
        baiduSpaceEntryUrl =self.Host# "https://m.taocaimall.com/taocaimall/appLongin.json"
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(baiduSpaceEntryUrl)
        loginBaiduUrl = self.appLongin1#"https://passport.baidu.com/?login";
        '''para = {"requestmodel":{"drivice": "android",
                "username": USER_NAME[0],
                "clientId": "cbe0cb9720d3d1a4f4e5e40ecb2c6435",
             "password": PASSWROD[0]
                }
                }

        postData = urllib.urlencode(para)
        '''
        postData="requestmodel={%22drivice%22:%22android%22,%22username%22:%22"+username+"%22,%22clientId%22:%22cbe0cb9720d3d1a4f4e5e40ecb2c6435%22,%22password%22:%22"+password+"%22}"
        text=self.do_get_post(loginBaiduUrl,postData)
        print text
        dicttext=json.loads(text)
        self.sessionid=dicttext["sessionid"]
        self.userId=dicttext["userId"]
        self.addrInfo=dicttext["addrInfo"]

        postData="requestmodel={%22drivice%22:%22android%22,%22clientid%22:%22cbe0cb9720d3d1a4f4e5e40ecb2c6435%22}"
        text = self.do_get_post(self.appLongin2, postData)
        postData=""
        text = self.do_get_post(self.appLongin3, postData)
        text = self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/address.json", postData)
        yy=json.loads(text)
        #yydic=yy.list
        self.telephone=yy['list'][0]["telephone"]

        # self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/goodscart_notify.json ", postData)
        # self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/account.json", postData)
        # self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/account_avatar.json", postData)
        # self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/message_unread_count.json", postData)
        # self.do_get_post("http://m.taocaimall.com/taocaimall/buyer/order_notify.json", postData)
        pass

    #------------------------------------查询订单------------------------------------
    def queryOrder(self):
        pass

    #------------------------------------查询积分------------------------------------
    def queryAccount(self):
        pass

    # ------------------------------------查询优惠卷------------------------------------
    htmltext=""
    def querydiscountCoupon(self):
        htmltext=""
        text = self.do_get_post(self.discountCouponUrl,"")
        mydirc=json.loads(text)
        mylist=mydirc["list"]
        for vo in mylist:
            vo["user"]=self.telephone
            htmltext=htmltext+self.htmltd.decode('utf-8').format(**vo).encode('utf-8')
            pass
        #print htmltext #这是拼装的table td
        self.saveHTML(self.htmlstart+self.htmlth+htmltext+self.htmlend,'taocaimao_%s.html'%time.strftime("%Y%m%d", time.localtime()) )

    allviewSignin=""
    #------------------------------------签到------------------------------------
    def signIn(self):

        time.sleep(3)#前面请求太多等待3秒再签到
        viewSignin="http://m.taocaimall.com/taocaimall/buyer/viewSignin.htm?sessionId=%s"%self.sessionid
        print viewSignin
        self.allviewSignin = self.allviewSignin+viewSignin+ self.telephone
        #============================== 查看签到开始
        req = urllib2.Request(viewSignin,
                              "")  # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.

        req.add_header('Host', 'm.taocaimall.com')
        req.add_header('Connection', 'keep-alive')
        #print "cookie：%s" % self.cookievalue
        req.add_header('Cookie', self.cookievalue)
        # req.add_header('Content-Length', '19')
        req.add_header('Accept', 'application/json, text/javascript, */*')
        req.add_header('Origin', 'http://m.taocaimall.com')
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('Referer', viewSignin)
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept-Language', 'zh-CN,en-US;q=0.8')
        resp = urllib2.urlopen(req)

        setcookie = resp.headers.headers[4]
        index = setcookie.find("JSESSIONID")
        signincookievalue = setcookie[index:index + 43]


        text = resp.read()
        # ==============================查看签到结束




        #text = self.do_get_post(viewSignin, "")
        index=text.find('xx=')
        xx=text[index:index+35]
        print xx
        postdata = "requestmodel=%7B%7D"
        Signinurl="http://m.taocaimall.com/taocaimall/buyer/signIn.json?sessionId=%s&%s&%s"%(self.sessionid,xx,postdata)
        print "Signinurl:%s"%Signinurl
        #text = self.do_get_post(Signinurl, "requestmodel=%7B%7D")

        postdata="requestmodel=%7B%7D"
        #=====================签到开始



        try:
            req = urllib2.Request(Signinurl)  # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.
            req.add_header('Host', 'm.taocaimall.com')
            req.add_header('Connection', 'keep-alive')
            print "cookie22：%s"%self.cookievalue
            print "cookie11：%s" % signincookievalue
            req.add_header('Cookie',signincookievalue)
            #req.add_header('Content-Length', '19')
            req.add_header('Accept', 'application/json, text/javascript, */*')
            req.add_header('Origin', 'http://m.taocaimall.com')
            req.add_header('X-Requested-With', 'XMLHttpRequest')
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Referer',    viewSignin)
            req.add_header('Accept-Encoding', 'gzip, deflate')
            req.add_header('Accept-Language', 'zh-CN,en-US;q=0.8')
            resp = urllib2.urlopen(req)


            text = resp.read()
            print text
        except ValueError:
            print '网络超时。。。。'
        #=====================签到结束
        pass

    #------------------------------------退出登录------------------------------------
    def appLongout(self):

        text=self.do_get_post(self.appLongoutUrl, "")
        dictinfo = json.loads(text)
        if(dictinfo["op_flag"]=="success"):
             print '%s,成功退出!'%self.user_now
        else:
            print  '%s,成功失败!'%self.user_now
        pass

    # ------------------------------------批量操作 签到------------------------------------
    def go_main(self,option_type):
        for i in range(self.user_index, 4):

            # 登录
            self.login(self.USER_NAME[i], self.PASSWROD[i])
            if option_type==1:
                # 查看积分 和签到
                self.signIn()
            elif (option_type==2):
                #查看优惠卷
                self.querydiscountCoupon()
            # 退出登录
            #self.appLongout()
            if i==3:
                print "全部账号签到完毕"
                print "要见到的地址\n"+self.allviewSignin
                exit
            else:
                #设定下一个账号登录间隔
                x = random.random() * 25
                print '%d秒后开始登录下一个账号'%x
                time.sleep(x)
    def test(self):
        list=[{"op_flag":"success","info":"操作成功","list":[{"id":"1868971","favorable_money":"12","origin_price":"29","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"vaid","begin_date":"2016-06-17","code":"625dc124","type":"普通优惠券","validity_date":"2016-06-24"},{"id":"1921884","favorable_money":"6","origin_price":"42","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"vaid","begin_date":"2016-06-22","code":"27dd8d27","type":"普通优惠券","validity_date":"2016-06-25"},{"id":"1930141","favorable_money":"10","origin_price":"69","useType":"3","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"vaid","useTypeInfo":"蔬果专区欢乐送","begin_date":"2016-06-23","code":"MTFkNzI4","type":"专区优惠券","validity_date":"2016-06-29"},{"id":"956946","favorable_money":"1","origin_price":"29","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-14","code":"MGZmYzVh","type":"普通优惠券","validity_date":"2016-06-21"},{"id":"956945","favorable_money":"2","origin_price":"29","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-13","code":"ZDFiNWYx","type":"普通优惠券","validity_date":"2016-06-20"},{"id":"1868970","favorable_money":"5","origin_price":"39","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-17","code":"70b51030","type":"普通优惠券","validity_date":"2016-06-20"},{"id":"956944","favorable_money":"2","origin_price":"29","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-12","code":"NTQyYTky","type":"普通优惠券","validity_date":"2016-06-19"},{"id":"1793855","favorable_money":"5","origin_price":"39","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-14","code":"bb5da141","type":"普通优惠券","validity_date":"2016-06-17"},{"id":"956943","favorable_money":"3","origin_price":"29","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-09","code":"MWJmMmUz","type":"普通优惠券","validity_date":"2016-06-16"},{"id":"1779856","favorable_money":"5","origin_price":"39","useType":"2","description":"凡满足本券使用金额且不与淘菜猫其他优惠同享（促销、满赠、换购、首单等）均可使用","timeFlag":"invaid","begin_date":"2016-06-13","code":"3844de4c","type":"普通优惠券","validity_date":"2016-06-16"}]},

              ]

    #--------------------------------导出清单 开始----------------------------
    htmlstart='''\
    <html>
    <head><!--pc--><title>python 获取淘菜猫的优惠卷</title><meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <style>
    table.dataintable {
       border: 1px solid #888888;
       border-collapse: collapse;
       font-family: Arial,Helvetica,sans-serif;
       margin-top: 10px;
       width: 100%;
    }
    table.dataintable th {
       background-color: #CCCCCC;
       border: 1px solid #888888;
       padding: 5px 15px 5px 5px;
       text-align: left;
       vertical-align: baseline;
    }
    table.dataintable td {
       background-color: #EFEFEF;
       border: 1px solid #AAAAAA;
       padding: 5px 15px 5px 5px;
       vertical-align: text-top;
    }
    </style>
    </head>
    <body>
    <table class="dataintable">
    '''
    htmlth='''\
    <tr>
        <th>user                   </th>
        <th>id                     </th>
        <th>favorable_money        </th>
        <th>origin_price           </th>
        <th>useType                </th>
        <th>description            </th>
        <th>timeFlag               </th>
        <th>begin_date             </th>
        <th>code                   </th>
        <th>type                   </th>
        <th>validity_date          </th>

    </tr>
    '''

    htmltd='''\
    <tr>
        <td>{user}</td>
      <td>{id}</td>
        <td>{favorable_money}</td>
        <td>{origin_price}</td>
        <td>{useType}</td>
        <td>{description}</td>
        <td>{timeFlag}</td>
        <td>{begin_date}</td>
        <td>{code}</td>
        <td>{type}</td>
        <td>{validity_date}</td>
    </tr>
    '''
    htmlend='''\
    <tr>
       <th colspan="11">分页代码       </th>
    </tr>
    </table>
    </body>
    </html>
    '''
    '''
    truncate()表示清空文件
write()写入文本
    '''
    def saveHTML(self,html,filename):
        #print html
        f = open(filename, 'a')
        #f.truncate()
        f.write(html)
        f.closed
        print '文件%s生成成功!'%filename
    pass


if __name__=="__main__":
    mao=qiwebTaoCaiMao()

    distext='''
    欢迎使用{淘菜猫智能系统Python版本}
    菜单指令【1、批量签到  , 2、批量生产优惠卷清单,3、设置账号起始位置,4、退出系统】
    '''
    print distext

    while True:
        menu= raw_input("请输入指令:")
        if menu=='1':
            # 签到
            mao.go_main(1)
        elif menu=='2':
            # 查了积分
            mao.go_main(2)
        elif menu=='3':
            pass
        elif menu=='4':
            exit
        else:
            print '你是在开玩笑吧，就没你想要的功能'





'''
Cache-Control: no-cache, no-store, max-age=0
Content-Language: en-US
Content-Type: application/json;charset=UTF-8
Date: Wed, 22 Jun 2016 04:48:44 GMT
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Pragma: no-cache
Server: nginx
Set-Cookie: JSESSIONID=5E201976C7F368884C38807FC00722C7; Path=/taocaimall/; HttpOnly
Content-Length: 483
Connection: Close

'''

