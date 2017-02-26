#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse,urllib.request,http.cookiejar

class sq:
    def PostUrlRequest(self,iUrl,iStrPostData):
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

    def GetUrlRequest(self,Url):
        header = {
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
                }
        req= urllib.request.Request(
                   url = Url,
                   headers = header)
        return urllib.request.urlopen(req).read().decode("UTF8")

