#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import redis
from tools.config.getConfig import getConfig

def con_redis():
	redis_conf = getConfig('redisdb')
	r = redis.Redis(host=redis_conf['host'],port=redis_conf['port'],password=redis_conf['password'],db=1)
return r