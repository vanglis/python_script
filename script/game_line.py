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
    config.read("userInfo.conf")
    environmentNum = config.get("userInfo","environmentNum")
    loginName = config.get("userInfo","loginName")
    pwd = config.get("userInfo","pwd")
    testStr = config.get("userInfo","testStr")
    amount = config.get("line","amount")
    line = config.get("line","line")
    userData = {
                'environmentNum':environmentNum,
                'loginName':loginName,
                'pwd':pwd,
                'testStr':testStr,
		        'amount':amount,
		        'line':line,
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
    num = int(input("押注次数: "))
    userData = GetConfig()                                      
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
                'back_url':'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_line',
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
    print(PostUrlRequest(urlLogin,strLoginInfo))
    GetUrlRequest('http://163test2-wap.stg2.24cp.com/?act=act_rank_1511&st=main&goUrl=%3Fact%3Dgame_line')
    print(cookie)
    for i in range(num):
        betUrl = 'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_line&st=play&amount='+userData['amount']+'&line='+userData['line']
        result = str(i)+": "+GetUrlRequest(betUrl)
        print(result)
        f = open("/data/python/script/logs/game_line.log",mode='a',encoding="UTF-8")
        f.write(result+"\n")
        f.close()
