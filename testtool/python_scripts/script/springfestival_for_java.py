#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

from urllib import parse
import json,sys
from Base import Urlpost

host = 'http://localhost:8080/GameSupport_151209_squib/act/squib'


def main():
	urls = ['getMatchCount()','addMatchCount()','getFirecrackerCount()','getFirecrackerRank()','getUserPrizeTotal()','newyearSquib()','updateSquibPrize()','getUserFirecrackerRecord()']
	for x in urls:
		print ('%s:%s'%(urls.index(x),x))
	index = input('please select Funtion:')
	if index not in ('0','1','2','3','4','5','6','7','q','Q'):
		print (u'输入错误,重新输入')
		main()
	elif index in ('q','Q'):
		sys.exit()
	funtion = urls[int(index)]
	print (funtion)
	re = eval(funtion)
	print (re.read())
	main()
	
def getMatchCount(): #获取用户火柴个数接口
	url = host+'/getMatchCount.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo}})})
	re = Urlpost.post(url,data)
	return re

def addMatchCount(): #添加用户火柴个数接口
	url = host+'/addMatchCount.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	ufrom = int(input('\tfrom:'))
	ukField = input('\tukField:')
	addCount = int(input('\taddCount:'))
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo,'from':ufrom,'ukField':ukField,'addCount':addCount}})})
	re = Urlpost.post(url,data)
	return re

def getFirecrackerCount(): #获取用户鞭炮个数接口
	url = host+'/getFirecrackerCount.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	useStatus = int(input('\tuseStatus:'))
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo,'useStatus':useStatus}})})
	re = Urlpost.post(url,data)
	return re

def getFirecrackerRank(): #获取燃放鞭炮排行信息接口
	url = host+'/getFirecrackerRank.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo}})})
	re = Urlpost.post(url,data)
	return re

def getUserPrizeTotal(): #获取用户获奖列表
	url = host+'/getUserPrizeTotal.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo}})})
	re = Urlpost.post(url,data)
	return re

def newyearSquib(): #燃放鞭炮接口
	url = host+'/newyearSquib.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	useMatchCount = int(input('\tuseMatchCount:'))
	userType = input('\tuserType:')
	channel = int(input('\tchannel:'))
	trackCode = input('\ttrackCode:')
	gameId = int(input('\tgameId:'))
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo,'useMatchCount':useMatchCount,'userType':userType,'channel':channel,'trackCode':trackCode,'gameId':gameId}})})
	re = Urlpost.post(url,data)
	return re

def updateSquibPrize(): #跑批更新奖池接口
	url = host+'/updateSquibPrize.do'
	re = Urlpost.post(url)
	return re

def getUserFirecrackerRecord(): #获取用户赠送鞭炮记录
	url = host+'/getUserFirecrackerRecord.do'
	userId = int(input('\tuserId:'))
	actNo = input('\tactNo:')
	data = parse.urlencode({'data':json.dumps({'body':{'userId':userId,'actNo':actNo}})})
	re = Urlpost.post(url,data)
	return re


if __name__ == "__main__":
	main()
