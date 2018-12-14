#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-04-28
Author: xiaohanfei
TODO: 流水采集校验
'''
import sys
from tools.db.dbmodule import conn

import logging

logging.basicConfig(
   level = logging.DEBUG, #将来布署到生产环境之后就修改成error级别了
   format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
   filename = '/home/www/logs/python/auto_test.log',  #日志存放的目录
)

time = '2016-04-27'
sql = "SELECT batch_no from game_customize_pool_batch_info WHERE raw_add_time LIKE '"+time+"%' AND `status`<>2;"
all_batch_no = conn('db_wlt_gameplatform',sql)
sum_prize_amount = 0
sum_recharge_amount = 0
for batch_no in all_batch_no:
    #print(batch_no['batch_no'])
    sql2 = "SELECT SUM(prize_amount) as prize_amount,sum(recharge_amount) as recharge_amount FROM game_customize_pool_log WHERE batch_no='"+batch_no['batch_no']+"';"
    amount = conn('db_wlt_gameplatform',sql2)
    prize_amount = amount[0]['prize_amount']
    recharge_amount = amount[0]['recharge_amount']
    recharge_amount = amount[0]['recharge_amount']
    if prize_amount == None:
       prize_amount = 0
    if recharge_amount == None:
       recharge_amount = 0   
    sum_prize_amount += prize_amount
    sum_recharge_amount += recharge_amount
print('sum_prize_amount:'+str(sum_prize_amount))
print('sum_recharge_amount:'+str(sum_recharge_amount))

