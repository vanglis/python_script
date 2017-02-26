#!/usr/bin/env python2.6
#-*-coding:utf-8-*-

import cookielib
import urllib,urllib2
import json

cj = cookielib.CookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
headers = {'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/33.0.1750.146 Safari/537.36'}
opener = urllib2.build_opener(cookie_support)
urllib2.install_opener(opener)

def post(url,data=None):
	try:
		data = urllib.urlencode(data)
		request = urllib2.Request(url,data)
		response = urllib2.urlopen(request)
		result = response.read()
		print result
		try:
			result = json.dumps(json.loads(result),ensure_ascii=False,indent=4)
		except Exception,e:
			result = result
		return result
	except Exception,e:
		print 'Exception:%s'%e
	

def login(name,passwd):
	strLoginInfo = {
	'accountType':'wlt',
	'loginName':name,
	'pwd':passwd,
	'vcodeValue':'',
	'vcodeId':'',
	'client_id':'IN_000002',
	'redirect_uri':'http://youxi29.stg2.24cp.com/?act=login&st=loginCallback&go_url=aHR0cDovL3lvdXhpMjkuc3RnMi4yNGNwLmNvbS8=',
	'response_type':'code',
	'platform':'WEB',
	'media_source':'',
	'display':'',
	'otherLogin':'QQ|ALIPAY|WEIBO|WEIXIN',
	'state':'_20150715150226631379',
	'isapp':'',
	'back_js':'',
	'back_url':'',
	'back_flag':'',
	'register_step2':'',
	'tabs':'paw|wlt|toa',
	'accountType':'wlt',
	'topBar':'',
	'footBar':'',
	'regFlag':'',
	'loginFlag':'',
	'otpFlag':''}
	urlLogin='http://passport2.stg2.wanlitong.com/pass-info/oauth2/wltLogin.shtml'
	re = post(urlLogin,strLoginInfo)
	print re



def racing(name,passwd,body):
	login(name,passwd)
	url1 = 'http://youxi29.stg2.24cp.com/?act=act_racing&st=confirm'
	body = {
        'one':0,
        'two':0,
        'three':0,
        'four':0,
        'five':0,
        'six':0}
	re1 = post(url1,body)
	print re1
	url2 = 'http://youxi29.stg2.24cp.com/?act=act_racing&st=get_score_coin'
	re2 = post(url2)
	print re2
	url3 = 'http://youxi29.stg2.24cp.com/?act=act_racing&st=result'
	re3 = post(url3)
	print re3


if __name__ == "__main__":
	name = '13262230550'
	passwd = '5413cc9ad92c5d2d9bba693133951f8f3d1a60ace84bec4d8c59dd6a0b50fbf7c259b191d425b03e93d2dd6ea50583c965d0f1493f37ecfaa32d1c9d63ea73bd37913f4d4ad19afaf918aaeba22ee1f336be0ab53d26e7e0d74ab3769206d62b52d20038f2c92356dfe156ce6aeff4ae831d90418091a51e12590bcb12575548'
	body = {
	'one':0,
	'two':0,
	'three':0,
	'four':0,
	'five':0,
	'six':0}
	racing(name,passwd,body)
