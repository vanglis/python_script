#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-12-24

@author: xiaohanfei
''' 
import urllib.parse,urllib.request,http.cookiejar,os
import logging

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
 try:
   f = open("/data/python/logs/git_checkInfo.log","r")
   contents = f.readlines()
   f.close()
   if contents == None:
      print('contents is None')
   else:
      message = ''.join(contents)
      recipient1 = 'ML_7213@pingan.com.cn'
      recipient2 = 'ML_10221@pingan.com.cn'
      recipient3 = 'ML_6396@pingan.com.cn'
      subject = ' 测试分支合并最新主干代码提醒,系统邮件请勿回复'
      Url = 'http://163testtool.stg2.24cp.com/sendemail/'
      PostData = {'recipient1':recipient1,'recipient2':recipient2,'recipient3':recipient3,'subject':subject,'message':message}
      r = PostUrlRequest(Url,PostData)
      print(r)
 except Exception as e:
   errorLogName = '/data/python/logs/error.log'
   log_format = '%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s'
   logging.basicConfig(filename = errorLogName,filemode = 'w',format = log_format,datefmt = '%Y-%m-%d %H:%M:%S %p',level = logging.DEBUG )
   logging.debug(e)
