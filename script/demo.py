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
toMail = 'ml_pinganwlt@pingan.com.cn'
subject = 'aaa'
content = 'test'
Url = 'http://devmail.stg2.wanlitong.com/MAIL/hbaseTest/testSendMail.action?toMail='+toMail+'&toName=liuyanwen&subject='+subject+'&content='+content
print(Url)
GetUrlRequest(Url)
