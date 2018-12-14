#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-03-23
Author: xiaohanfei
TODO: 疯狂夺宝押注脚本
'''
from Base.Login import wap_login
from Base.Urlpost import post
import json
import urllib.request
from tools.log import w_log
import os
from multiprocessing import Pool

def play(username,pwd):
    host = 'http://163test2-wap.stg2.24cp.com'
    wap_login(host,username,pwd)
    play_url = host+'/?act=game_crazycheckpoints&st=play'
    data = {'line':'5','amount':'500'}
    output = post(play_url,data).read().decode()
    print(output)
    
if __name__ == '__main__':
   p = Pool(processes=6)
   p.apply_async(play,args=('youxi0001','youxi0001'))
   p.close()
   p.join()

