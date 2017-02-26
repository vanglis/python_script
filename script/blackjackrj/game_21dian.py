#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-6-25

@author: xiaohanfei
''' 
import urllib.parse,urllib.request,http.cookiejar
import base64

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
    betstr = "aaa"
    encodestr = base64.b64encode(str(betstr))
    print(encodestr)
    for i in range(num):
        betUrl = 'http://'+userData['testStr']+userData['environmentNum']+'-wap.stg2.24cp.com/?act=game_line&st=play&amount='+userData['amount']+'&line='+userData['line']
        result = str(i)+": "+GetUrlRequest(betUrl)
        print(result)
        f = open("/data/python/script/logs/game_line.log",mode='a',encoding="UTF-8")
        f.write(result+"\n")
        f.close()
