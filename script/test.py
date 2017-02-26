#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-10-19
 
@author: xiaohanfei
'''
import urllib.parse,urllib.request,http.cookiejar
import random
import time
 
def UrlRequest(Url,myip): 
    header = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
              'X-Forwarded-For':myip
              } 
    req= urllib.request.Request( 
               url = Url, 
               headers = header) 
    return urllib.request.urlopen(req).read().decode("utf-8")
                                       
#设置cookie  
cookie = http.cookiejar.CookieJar() 
cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(cookieProc) 
urllib.request.install_opener(opener)
def setip():
   a = random.randint(0,255)
   b = random.randint(0,255)
   c = random.randint(0,255)
   d = random.randint(0,255)
   ip = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
   return ip

if __name__ == "__main__":
   for i in range(1):
      #try:
         url='http://www.jjxmw.com/public/ajax.aspx?action=addvote&id=230&type=add&_=1445253350962'
         myip = setip()
         print(myip)
         print(UrlRequest(url,myip))
         print('ticket secess:'+str(i))
      #except Exception:
       #  continue
    #time.sleep(0.5)
