#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-07-14
Author: xiaohanfei
TODO: 拯救小天使
'''
from Base.Login import wap_login
from Base.Urlpost import post
import json
from urllib import parse
import os
from multiprocessing import Pool
import logging

logging.basicConfig(  
   level = logging.DEBUG, #将来布署到生产环境之后就修改成error级别了
   format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',  
   filename = '/home/www/django.log',  #日志存放的目录
)


def play(username,pwd):
    host = 'http://163test33-wap.stg2.24cp.com'
    wap_login(host,username,pwd)
    url = 'http://163test33-wap.stg2.24cp.com/?act=game_saveangel&st=play'
    data = {'amount':2500,'isFree':0}
    data = parse.urlencode(data)
    for i in range(1000):
      r = post(url,data).read().decode()
      output = '\033[1;31;40m ['+str(i)+']: \033[0m'+r
      print(output)
     # r = json.loads(r)
     # freeNum = r['freeNum']
     # if freeNum > 0:
     #    data = {'amount':2500,'isFree':1}
      
if __name__ == '__main__':
   play('youxi0003','youxi0003')
