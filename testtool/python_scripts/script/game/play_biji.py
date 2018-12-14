#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-01-18
Author: xiaohanfei
TODO: 比鸡押注脚本
'''
from Base.Login import wap_login
from Base.Urlpost import post
import json
import urllib.request
from tools.log import w_log
import os
import threading
class Thread(threading.Thread):
    def __init__(self,username,pwd):
        threading.Thread.__init__(self)
        self.username = username
        self.pwd = pwd
    

    def run(self):
        host = 'http://163test-wap.stg2.24cp.com'
        wap_login(host,self.username,self.pwd)
        url_enter_room = host+'/?act=game_biji&st=enter_room&id=1000750'
        url_deal = host+'/?act=game_biji&st=deal'
        url_pipei = host+'/?act=game_biji&st=pipei_poker'
        post(url_enter_room)
        for i in range(10000):
           r_deal = post(url_deal).read().decode()
           r_deal = json.loads(r_deal)
           r_deal = r_deal['statusCode']
           if r_deal == '2000':
              print(r_deal)
           else:
              r_pipei = post(url_pipei).read().decode()
              r_pipei = json.loads(r_pipei)
              print(r_pipei)
              card1 = r_pipei['card3']
              card1 = '[["'+card1[0]+'","'+card1[1]+'","'+card1[2]+'"],["'+card1[3]+'","'+card1[4]+'","'+card1[5]+'"],["'+card1[6]+'","'+card1[7]+'","'+card1[8]+'"]]'
              card1 = urllib.request.quote(card1)
              card1 = urllib.request.quote(card1)
              url_bipai = host+'/?act=game_biji&st=bipai&poker='+card1
              r_bipai = post(url_bipai).read().decode()
              output = '\033[1;31;40m ['+str(i)+']: \033[0m'+r_bipai
              w_log.w_log('biji',output)
              print(output)
if __name__ == '__main__':
   username = ['youxi0001','youxi0002','youxi0003','youxi0004','youxi0005']
   for x in range(5):
     t = Thread(username[x][0:],username[x][0:])
     t.start()

