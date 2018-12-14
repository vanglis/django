#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-01-18
Author: xiaohanfei
TODO: wap卡当押注脚本
'''
from Base.Login import wap_login
from Base.Urlpost import post
import json
from urllib import parse

host = 'http://163test2-wap.stg2.24cp.com'

wap_login(host,'youxi0003','youxi0003')

url_get_two = host+'/?act=game_crazystuck&st=get_two'
url_get_three = host+'/?act=game_crazystuck&st=get_three'

data1 ={'amount':100}
data1 = parse.urlencode(data1)
data2 = {'double':1}
data2 = parse.urlencode(data2)
for i in range(1000):
   r_get_two = post(url_get_two,data1).read().decode()
   print(r_get_two)
   r_get_three = post(url_get_three,data2).read().decode()
   print(r_get_three)


