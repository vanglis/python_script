#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-6-12

@author: xiaohanfei
''' 
import time
import sys
import gzip
import socket
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
 
class HttpTester:
    def __init__(self, timeout=10, addHeaders=True):
        socket.setdefaulttimeout(timeout)   
        self.__opener = urllib.request.build_opener()
        urllib.request.install_opener(self.__opener)
        if addHeaders: self.__addHeaders()
    def __error(self, e):
        '''´íÎó´¦Àí'''
        print(e)
 
    def __addHeaders(self):
        '''Ìí¼ÓÄ¬ÈÏµÄ headers.'''
        self.__opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'),
                                    ('Connection', 'keep-alive'),
                                    ('Cache-Control', 'no-cache'),
                                    ('Accept-Language:', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
                                    ('Accept-Encoding', 'gzip, deflate'),
                                    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                                    ('Cookie', 'from=inner; YOUXISID=20d3b07276b2e7a6c4bb31266e12f695ccbe06b3; PHPSESSID=f5ojq702lfao2ke8fppo8ugan2;')]
    def __decode(self, webPage, charset):
        '''gzip½âÑ¹£¬²¢¸ù¾ÝÖ¸¶¨µÄ±àÂë½âÂëÍøÒ³'''
        if webPage.startswith(b'\x1f\x8b'):
            return gzip.decompress(webPage).decode(charset)
        else:
            return webPage.decode(charset)
 
    def addCookiejar(self):
        '''Îª self.__opener Ìí¼Ó cookiejar handler¡£'''
        cj = http.cookiejar.CookieJar()
        self.__opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
 
    def addProxy(self, host, type='http'):
        '''ÉèÖÃ´úÀí'''
        proxy = urllib.request.ProxyHandler({type: host})
        self.__opener.add_handler(proxy)
 
    def addAuth(self, url, user, pwd):
        '''Ìí¼ÓÈÏÖ¤'''
        pwdMsg = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        pwdMsg.add_password(None, url, user, pwd)
        auth = urllib.request.HTTPBasicAuthHandler(pwdMsg)
        self.__opener.add_handler(auth)
 
    def get(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP GET ·½·¨'''
        if params: url += '?' + urllib.parse.urlencode(params)
        request = urllib.request.Request(url)
        for k,v in headers.items(): request.add_header(k, v)    # ÎªÌØ¶¨µÄ request Ìí¼ÓÖ¸¶¨µÄ headers
 
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.__error(e)
        else:
            return self.__decode(response.read(), charset)
 
    def post(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP POST ·½·¨'''
        params = urllib.parse.urlencode(params)
        request = urllib.request.Request(url, data=params.encode(charset))  # ´ø data ²ÎÊýµÄ request ±»ÈÏÎªÊÇ POST ·½·¨¡£
        for k,v in headers.items(): request.add_header(k, v)
 
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.__error(e)
        else:
            return self.__decode(response.read(), charset)
 
if __name__=="__main__":
    ht=HttpTester()
    ht.addCookiejar()
    url = input('url: ')
    for i in range(1):
            print(i)
            a=ht.get(url)
            print(a)
