#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

from Base import Urlpost,Login
from urllib import parse
import time,sys

class Play_game():
	"""docstring for Play_game"""
	def __init__(self):
		self.timeStamp=time.time()*100
		self.Url = input('Url:').strip(' ')
		self.fp = parse.urlparse(self.Url)
		if self.fp.scheme == '' or self.fp.query == '':
			print (u'请规范Url输入:\nhttp://{domain}/?act=game_name')
			sys.exit()
		self.loginname = input('loginname:').strip(' ')
		self.pwd = input('pwd:').strip(' ')

	def main(self):
		self.host = parse.urlunparse((self.fp.scheme,self.fp.netloc,'','','',''))
		if Login.wap_login(self.host,self.loginname,self.pwd):
			game_name = self.fp.query.split('&')[0].split('=')[1]
			if game_name in ('game_niuniu','guesswap','game_poker','game_crazystuck','game_circus','game_rolldice2','game_crazycheckpoints','slot','game_line','pinballwap'):
				self.ranges = input(u'输入循环次数(1~1000):')
				if self.ranges in map(lambda x:str(x),range(1,1001)):
					self.ranges = int(self.ranges)
					eval('self.'+game_name)()
				else:
					print (u'请规范输入(1~1000)')
					sys.exit()	
			else:
				print ('Game_Name not match')
		else:
			sys.exit()

	def post(self,url,data=None):
		result = Urlpost.post(url,data)
		try:
			result = Urlpost.jsondecode(result.read())
			return result
		except Exception as e:
			result = Urlpost.post(self.host+result['Location'])
			result = Urlpost.post(self.host+result['Location'])
			result = Urlpost.jsondecode(Urlpost.post(url,data).read())
			return result

	def game_niuniu(self):
		amount = input('amount:')
		url = self.host+'/?act=game_niuniu&st=play&amount={amount}'.format(amount=amount)
		for x in range(self.ranges):
			result = self.post(url)
			print (result)

	def guesswap(self):
		amount = input('amount:')
		utype = input('type(small or same or large ?):')
		url = self.host+'/?act=guesswap&st=guess'
		data = {'type':utype,'amount':amount,'newTag':0}
		for x in range(self.ranges):
			result = self.post(url,parse.urlencode(data))
			print (result)

	def game_poker(self):
		amount = input('amount:')
		url = self.host+'/?act=game_poker&st=getCard&guessFlag=0&amount={amount}&timeStamp={timeStamp}'.format(amount=amount,timeStamp=self.timeStamp)
		for x in range(self.ranges):
			result = self.post(url)
			print (result)

	def game_crazystuck(self):
		amount = input('amount:')
		url = self.host + '/?act=game_crazystuck&st=get_two'
		data = {'amount':amount,'timeStamp':self.timeStamp}	
		for x in range(self.ranges):
			result = self.post(url,parse.urlencode(data))
			url1 = self.host + '/?act=game_crazystuck&st=get_three'
			data = {'double':1,'amount':amount}
			result = self.post(url,parse.urlencode(data))
			print (result)

	def game_circus(self):
		amount = input('amount:')
		url = self.host+'/?act=game_circus'
		data = {'act':'game_circus','st':'start','amount':amount,'isNewUser':1}
		for x in range(self.ranges):
			result = self.post(url,parse.urlencode(data))
			print (result)

	def game_rolldice2(self):
		amount = input('amount:')
		utype = input('type(small or same or large ?):')
		url = self.host+'/?act=game_rolldice2&st=play&amount={amount}&type={type}'.format(amount=amount,type=utype)
		for x in range(self.ranges):
			result = self.post(url)
			print (result)

	def game_crazycheckpoints(self):
		amount = input('amount:')
		line = input('line:')
		url = self.host+'/?act=game_crazycheckpoints&st=play'
		data = {'reqAppId':1,'reqTime':11,'custString':'custString','line':line,'amount':amount}
		for x in range(self.ranges):
			result = self.post(url,parse.urlencode(data))
			print (result)

	def slot(self):
		amount = input('amount:')
		url = self.host+'/?act=slot&st=start'
		data = {'act':'slot','st':'start','amount':amount,'isNewUser':1}
		for x in range(self.ranges):
			result = self.post(url,parse.urlencode(data))
			print (result)

	def game_line(self):
		amount = input('amount:')
		line = input('line:')
		url = self.host+'/?act=game_line&st=play&amount={amount}&line={line}&isNewUser=false&timestamp={timeStamp}'.format(amount=amount,line=line,timeStamp=self.timeStamp)
		for x in range(self.ranges):
			result = self.post(url)
			print (result)

	def pinballwap(self):
		amount = input('amount:')
		url = self.host+'/?act=pinballwap&act=pinballwap&st=play_once&amount={amount}&newer=1&rndnum=825134'.format(amount=amount)
		for x in range(self.ranges):
			result = self.post(url)
			print (result)


if __name__ == '__main__':
	game = Play_game()
	game.main()
