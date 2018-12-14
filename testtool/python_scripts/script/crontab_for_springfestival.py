#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

from urllib import parse
import sys,time,json
from Base import Urlpost,Login
import time,random,math
from tools.db.dbmodule import conn
import threading

php_host = 'http://164test11-wap.stg2.24cp.com'
java_host = 'http://localhost:8080/GameSupport_151209_squib/act/squib'
useMatchCount = 100
amount = 20000


prize_list = [
{"prizeId":7218,"condition":"100,150,200,250,300,350,400,450,500,550"},  #30元T点
{"prizeId":7220,"condition":"200,300,400,500"},	#50元T点
{"prizeId":7222,"condition":"300,500,700"}, #移动电源
{"prizeId":7224,"condition":"400,700"}, #电压力锅
{"prizeId":7226,"condition":"3600"} #iPhone6s
] 

prize_name = {
	'7218':'30元T点',
	'7220':'50元T点',
	'7222':'移动电源',
	'7224':'电压力锅',
	'7226':'iPhone6s'
}

def main(loginName,userId):
	Login.wap_login(php_host,loginName,'c13579')
	count = getmatch()  #0
	con = math.floor(count/5000)
	A = lambda x:x if x <= 5000 else x%5000
	nowcon = A(count)
	print ('第%s轮,当前为:%s,总数量:%s'%(con+1,nowcon,count))
	update_prize()
	for x in prize_list:
		prizeId = x['prizeId']
		condition = [int(y) for y in x['condition'].split(',')]
		for z in condition:
			if nowcon>=z:
				print (prize_name[str(prizeId)])
				break
	url = php_host+'/?act=act_springfestival&st=start_firecracker&useMatchCount={useMatchCount}'.format(useMatchCount=useMatchCount)
	result = Urlpost.post(url).read()
	print ('\n%s'%Urlpost.jsondecode(result))
	re = json.loads(result.decode())
	code = re['code']
	if code == 6: #鞭炮数量不足
		play_game(3)
		main(loginName,userId)
	elif code == 9: #火柴数量不足,测试购买免费火柴
		print ('buy')
		buy_match(1)
		time.sleep(1)
		update_prize()
		main(loginName,userId)
	elif code == 3:
		time.sleep(1)
		main(loginName,userId)
	else:#火柴数量不足,测试购买收费火柴
		buy_match(1)


def buy_match(ufrom=0):  #ufrom:0:免费;1:收费
	ukField = 'TT'.join(str(x) for x in random.sample(range(1000),5))
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':'SNAC100254','from':ufrom,'ukField':ukField,'addCount':10}})})
	re = Urlpost.post(java_host+'/addMatchCount.do',data)
	result = Urlpost.jsondecode(re.read())
	return result

def play_game(count=10):
	A = lambda self,x,n:x if n <= 0 else self(self,Urlpost.jsondecode(Urlpost.post(php_host+'/?act=game_niuniu&st=play&amount={amount}'.format(amount=amount)).read()),n=n-1)
	A(A,amount,count)

def getmatch():
	sql = 'SELECT SUM(add_count) AS count FROM game_activity_match_details where match_from = 1;' #当前购买的收费火柴
	re = conn('db_wlt_gameplatform',sql)[0]['count']
	return re


def update_prize():
	url = java_host+'/updateSquibPrize.do'
	data = parse.urlencode({'data':json.dumps({'body':{}})})
	re = Urlpost.post(url,data)
	result = Urlpost.jsondecode(re.read())
	return result


if __name__ == '__main__':
	with open('userinfo.conf','r') as fp:
		for x in fp.readlines():
			info = x.strip('\n').split(',')
			loginName = info[0]
			userId = int(info[1])
			if Login.wap_login(php_host,loginName,'c13579'):
					if main(loginName,userId) == False:
						continue

