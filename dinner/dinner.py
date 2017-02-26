#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-6-12

@author: xiaohanfei
''' 
import urllib.parse,urllib.request,http.cookiejar
import datetime

def GetUrlRequest(iUrl,iStrPostData): 
    postdata=urllib.parse.urlencode(iStrPostData) 
    postdata=postdata.encode(encoding='UTF8') 
    header = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'} 
    req= urllib.request.Request( 
               url = iUrl, 
               data = postdata, 
               headers = header) 
    return urllib.request.urlopen(req).read().decode("UTF8")

def UrlRequest(Url): 
    header = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'} 
    req= urllib.request.Request( 
               url = Url, 
               headers = header) 
    return urllib.request.urlopen(req).read().decode("UTF8")
                                       
#设置cookie  
cookie = http.cookiejar.CookieJar() 
cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(cookieProc) 
urllib.request.install_opener(opener)

#登录信息  
strLoginInfo = {'user_name':'ex-xiaohanfei001',
                'user_password':'123456'
                  }
urlLogin='http://dinner.stg2.wanlitong.com/index.php?at=user&st=login' 
GetUrlRequest(urlLogin,strLoginInfo)

strDinnerInfo = {'cook_id':'227'}
urlDinner='http://dinner.stg2.wanlitong.com/index.php?at=admin&st=getfood_action'
Result = GetUrlRequest(urlDinner,strDinnerInfo)
t = str(datetime.datetime.now())
f = open('/data/python/logs/dinner.py.log','r+')
f.write("["+t+"] "+Result)
f.close()


