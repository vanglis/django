#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import rsa,binascii
from Base.Urlpost import post
from urllib import parse
from tools.config.getConfig import getConfig

passportPubKey = getConfig('passportPubKey')['passportpubkey']

def wap_login(host,loginName,pwd):
	login_url = host+'/?act=user&st=login'
	veiw_url =  parse.urlparse(parse.unquote(post(login_url)['Location']))
	query = dict(set([tuple(x.split('=',1)) for x in veiw_url.query.split('&') if x.split('=',1)[0] not in ('st','mamc')]))
	query['redirect_uri'] = query['redirect_uri']+'&st=login_callback'
	post(parse.urlunparse((veiw_url.scheme,veiw_url.netloc+':8080',veiw_url.path,veiw_url.params,veiw_url.query,veiw_url.fragment))) 
	url = 'http://passport2.stg2.24cp.com:8080/pass-info/oauth2/loginPassport.shtml'
	data = {
			'accountType':'paw',
			'loginName':loginName,
			'pwd':encryption(pwd),
			'vcodeValue':'',
			'vcodeId':'',
			'back_js':'',
			'register_step2':'',
			'tabs':'paw|wlt|toa',
			'accountType':'paw',
			'topBar':'',
			'footBar':'',
			'regFlag':'',
			'loginFlag':'',
			'otpFlag':''
			}
	data.update(query)
	data = parse.urlencode(data)
	result = post(url,data)
	try:
		Location = result['Location']
		result2 = post(Location).read()
		return True
	except Exception as e:
		re = result.read()
		if re.find('20004') >= 0:
			print (u'用户名或登录密码错误')
			return False
		elif re.find('0049') >= 0:
			print (u'登录名不存在')
			return False
		elif re.find('0060') >= 0:
			print (u'密码不可为空')
			return False

def encryption(pwd): #RSA加密 
	rsaPublickey = int(passportPubKey, 16)
	pub_key = rsa.PublicKey(rsaPublickey,65537)
	base_encrypted = binascii.b2a_hex(rsa.encrypt(pwd.encode(encoding="utf-8"),pub_key))
	return base_encrypted

if __name__ == '__main__':
	wap_login('http://164test4-wap.stg2.24cp.com','fkfp','abc123')
