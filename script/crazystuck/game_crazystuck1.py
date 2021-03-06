#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-6-25

@author: xiaohanfei
''' 
import urllib.parse,urllib.request,http.cookiejar
import configparser

def GetConfig():
    config = configparser.ConfigParser()
    config.read("userInfo1.conf")
    environmentNum = config.get("userInfo","environmentNum")
    loginName = config.get("userInfo","loginName") 
    pwd = config.get("userInfo","pwd")
    testStr = config.get("userInfo","testStr")
    amount = config.get("crazystuck","amount")
    double = config.get("crazystuck","double")
    userData = {
		'environmentNum':environmentNum,
		'loginName':loginName,
		'pwd':pwd,
		'testStr':testStr,
		'amount':amount,
		'double':double,
	      }
    return userData

def PostUrlRequest(iUrl,iStrPostData): 
    postdata=urllib.parse.urlencode(iStrPostData) 
    postdata=postdata.encode(encoding='UTF8') 
    header = {
              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
            } 
    req= urllib.request.Request( 
               url = iUrl, 
               data = postdata, 
               headers = header) 
    return urllib.request.urlopen(req).read().decode("UTF8")

def GetUrlRequest(Url): 
    header = {
              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
            }  
    req= urllib.request.Request( 
               url = Url, 
               headers = header) 
    return urllib.request.urlopen(req).read().decode("UTF8")

if __name__ == "__main__":
#    environmentNum = input("游戏测试环境号: ")
#    loginName = input("loginName: ")
#    pwd = input("pwd: ")
    userData = GetConfig()
    num = int(input("押注次数: "))
                                       
#设置cookie  
    cookie = http.cookiejar.CookieJar() 
    cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
    opener = urllib.request.build_opener(cookieProc) 
    urllib.request.install_opener(opener)

#登录信息  
    strLoginInfo = {'accountType':'paw',
                'loginName':userData['loginName'],
                'pwd':userData['pwd'],
                'vcodeValue':'',
                'vcodeId':'',
                'client_id':'IN_000005',
                'redirect_uri':'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=login&st=login_callback',
                'response_type':'code',
                'platform':'WEB',
                'media_source':'',
                'display':'mobile',
                'otherLogin':'QQ|WEIBO',
                'state':'eyJzdGF0ZSI6ImU4NTg0NDY5MjZlYjQxZmFmYTRjZDg5ZDU1ZjIzOWNlIiwiZnJvbSI6IiIsImFwcGtleSI6IiIsInNlcnZlcklkIjoiIiwibG9naW5Tb3VyY2UiOiIifQ==',
                'isapp':'1',
                'back_js':'',
                'back_url':'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_crazystuck',
                'back_flag':'1',
                'register_step2':'',
                'tabs':'paw|wlt|toa',
                'accountType':'paw',
                'topBar':'',
                'footBar':'',
                'regFlag':'',
                'loginFlag':'',
                'otpFlag':''
                  } 
    urlLogin='http://passport2.stg2.24cp.com:8080/pass-info/oauth2/loginPassport.shtml' 
    PostUrlRequest(urlLogin,strLoginInfo)

    for i in range(num):
        getTowInfo = {'amount':userData['amount']}
        urlKd1 = 'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_crazystuck&st=get_two'
        result1 = str(i)+": "+PostUrlRequest(urlKd1,getTowInfo)
        print(result1)
        f = open("/data/python/script/logs/game_crazystuck.log",mode='a',encoding="UTF-8")
        f.write(result1+"\n")
        f.close()

        urlKd2 = 'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_crazystuck&st=get_three'
        getThreeInfo = {'double':userData['double'],'amount':userData['amount']}
        result2 = str(i)+": "+PostUrlRequest(urlKd2,getThreeInfo)
        print(result2)
        f = open("/data/python/script/logs/game_crazystuck.log",mode='a',encoding="UTF-8")
        f.write(result2+"\n")
        f.close()
