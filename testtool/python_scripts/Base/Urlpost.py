#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import json,http.cookiejar
from urllib import request

class RedirctHandler(request.HTTPRedirectHandler):
	"""docstring for RedirctHandler"""
	def http_error_301(self, req, fp, code, msg, headers):
		pass
	def http_error_302(self, req, fp, code, msg, headers):
		return headers

cj = http.cookiejar.CookieJar()
cookie_support = request.HTTPCookieProcessor(cj)
httpHandler = request.HTTPHandler(debuglevel=1) #调试信息 打开=1，关闭=0 
httpsHandler = request.HTTPSHandler(debuglevel=1) #调试信息 打开=1，关闭=0 
opener = request.build_opener(httpHandler, httpsHandler,cookie_support,RedirctHandler) 
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36')]
request.install_opener(opener) 

def post(url,data=None):
	response = None
	try:
		A = lambda x:x.encode(encoding="utf-8") if x != None else None
		req = request.Request(url,A(data))
		response = opener.open(req,timeout = 30)
		return response
	except request.URLError as e:
		if hasattr(e,'code'):
			error_info = e.code
			print ('code%s'%error_info)
		elif hasattr(e,'reason'):
			error_info = e.reason
			print ('reason%s'%error_info)

def jsondecode(inputstr):
	try:
		outputstr = json.dumps(json.loads(inputstr.decode()),ensure_ascii=False,indent=4)
		return outputstr
	except Exception as e:
		return inputstr
