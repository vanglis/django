#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import memcache
from tools.config.getConfig import getConfig

def con_memcache():
	memcache_conf = getConfig('memcachedb')
	clt = eval('[\''+memcache_conf['host']+':'+memcache_conf['port']+'\']')
	mc = memcache.Client(clt,debug=0)
	print (mc.get('GAMEAPP.24CAIPIAO.COM:temp:GAME_3850_GET_REWARD_CONFIG'))

if __name__ == '__main__':
	con_memcache()