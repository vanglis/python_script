#usr/bin/env python
#_*_ coding:utf-8 _*_

#chenxuedong

import urllib2
import urllib

url = 'http://youxi61-wap.stg2.24cp.com/?act=game_crazycheckpoints&st=fourxfour'
a=respone.read()

user_agent = 'Mozilla/4.0(compatible;MSIE5.5;Windows NT)'
headers = {'User-Agent':user_agnet}
def getData(url):
	try:
		rep = urllib2.Request(url,None,headers)
		respone = urllib2.urlopen(rep)
		return respone.read()
	except urllib2.URLError as e:
	print e
print a

getData()























