#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-01-20
Author: xiaohanfei
TODO: 帐户添加彩金、挺逗、T点、T币
'''
import sys
from tools.db.dbmodule import conn
import logging

logging.basicConfig(  
   level = logging.DEBUG, #将来布署到生产环境之后就修改成error级别了
   format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',  
   filename = '/home/www/django.log',  #日志存放的目录
)

def up_user_account(username,amount,type_id):
    se_user_info = "SELECT user_id FROM `t_user` WHERE name = '%s'" % (username)
    CP_ID = conn('db_wlt_caipiao',se_user_info)
    print('彩票user_id:'+str(CP_ID))
    logging.debug('彩票user_id:'+str(CP_ID))
    CP_ID = CP_ID[0]['user_id']
    select_user_sql = "SELECT GAME_ID,UID FROM passport_relationship WHERE CP_ID = '%s'" % (CP_ID)
    r = conn('db_24cp_auth',select_user_sql)
    passport_id = r[0]['UID']
    userid = r[0]['GAME_ID']
    print('游戏user_id:'+str(userid))
    logging.debug('游戏user_id:'+str(userid))
    if type_id == '1':
        output = up_tingdou(amount,userid)
    elif type_id == '2':
        output = up_td(passport_id,amount)
    elif type_id == '3':
        output = up_tb(amount,userid)
    elif type_id == '4':
        output = up_cj(CP_ID,amount)
    else:
     print('金额类型不正确')
    return output

def up_user_account2(gameid,amount,type_id):
    select_user_sql = "SELECT CP_ID,UID FROM passport_relationship WHERE GAME_ID = '%s'" % (gameid)
    r = conn('db_24cp_auth',select_user_sql)
    passport_id = r[0]['UID']
    CP_ID = r[0]['CP_ID']
    print('彩票user_id:'+str(CP_ID))
    logging.debug('彩票user_id:'+str(CP_ID))
    if type_id == '1':
        output = up_tingdou(amount,gameid)
    elif type_id == '2':
        output = up_td(passport_id,amount)
    elif type_id == '3':
        output = up_tb(amount,gameid)
    elif type_id == '4':
        output = up_cj(CP_ID,amount)
    else:
     print('金额类型不正确')
    return output

def up_tingdou(amount,userid):
    up_tingdou_sql = "UPDATE game_user_account SET total_amount='%s', avail_amount='%s' WHERE userid='%s';" % (amount,amount,userid)
    conn('db_wlt_gameplatform',up_tingdou_sql)
    se_tingdou_sql = "SELECT total_amount FROM game_user_account WHERE userid='%s';" % (userid)
    r = conn('db_wlt_gameplatform',se_tingdou_sql)
    r = r[0]['total_amount']
    return r

def up_td(passport_id,amount):
    se_td_sql = "SELECT * FROM points_user_total WHERE passport_id='%s';" % (passport_id)
    r = conn('db_wlt_gamepoint',se_td_sql)
    if r == []:
       in_td_sql = "INSERT INTO `points_user_total` (`id`, `passport_id`, `points`, `used_points`, `overdue_date`, `delete_flag`, `raw_add_time`, `raw_update_time`, `type`) VALUES ('', '%s', '%s', '0', '0000-00-00 00:00:00', '0', now(), now(), '1');" % (passport_id,amount)
       conn('db_wlt_gamepoint',in_td_sql)
    else:
       up_td_sql = "UPDATE points_user_total SET points='%s' WHERE passport_id='%s';" % (amount,passport_id)
       conn('db_wlt_gamepoint',up_td_sql)
    r = conn('db_wlt_gamepoint',se_td_sql)
    r = r[0]['points']
    return r

def up_tb(amount,userid):
    up_tb_sql = "UPDATE game_customize_user_account SET available_coin='%s' WHERE user_id='%s';" % (amount,userid)
    conn('db_wlt_gameplatform',up_tb_sql)
    se_tb_sql = "SELECT * FROM game_customize_user_account WHERE user_id='%s';" % (userid)
    r = conn('db_wlt_gameplatform',se_tb_sql)
    r = r[0]['available_coin']
    return r

def up_cj(CP_ID,amount):
    up_cj_sql = "UPDATE t_user_amount SET amount='%s' WHERE user_id='%s';" % (amount,CP_ID)
    conn('db_wlt_caipiao',up_cj_sql)
    se_cj_sql = "SELECT * FROM t_user_amount WHERE user_id='%s';" % (CP_ID)
    r = conn('db_wlt_caipiao',se_cj_sql)
    r = r[0]['amount']
    return r
if __name__ == "__main__":
 try:
    print(
        '''
        脚本用于更新账号余额，example：python up_user_account.py [param1] [param2] [param3]
        [param1] 登陆用户名
        [param2] 金额
        [param3] 类型(挺逗=>1|T点=>2|T币=>3|彩金=>4)
        '''
    )
    
    username = sys.argv[1]
    amount = sys.argv[2]
    type_id = sys.argv[3]
    se_user_info = "SELECT user_id FROM `t_user` WHERE name = '%s'" % (username)
    user_id = conn('db_wlt_caipiao',se_user_info)
    if user_id:
      r = up_user_account(username,amount,type_id)
      print("帐户金额更新成功，变更后的金额为:")
      logging.debug(r)
      print(r)
    else:
      gameid = username
      r = up_user_account2(gameid,amount,type_id)
      print("帐户金额更新成功，变更后的金额为:")
      logging.debug(r)
      print(r)
 except Exception as e:
      print(e)
      #logging.debug(e)
      print("请输入正确的参数")