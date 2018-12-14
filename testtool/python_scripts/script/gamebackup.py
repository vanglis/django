#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2017-02-14
Author: xiaohanfei
TODO: 人机游戏sql备份脚本
'''
import sys,os,time
import subprocess
import logging
import configparser

logging.basicConfig(  
   level = logging.DEBUG, #将来布署到生产环境之后就修改成error级别了
   format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',  
   filename = '/home/www/dbbackup.log',  #日志存放的目录
)

dbuser = "app_gameplatform"
dbpwd = "game12345"
dbhost = "21.58.201.191"
db = "db_wlt_gameplatform"

def Done():
    config = configparser.ConfigParser()
    config.read(sys.path[0]+"/config/game.conf")
    gamenames = config.options("gameid")
    filepath = "/home/www/gamebackup/"
    if not os.path.exists(filepath):
     os.mkdir(filepath)
    for gamename in gamenames:
       backname = gamename+str(time.strftime("%Y%m%d",time.localtime()))+".sql"
       backfile = filepath+backname
       gameid = config.get("gameid",gamename)
       custid = config.get("custid",gamename)
       SqlBackup(dbuser,dbhost,dbpwd,db,gamename,gameid,custid,backfile)
    return "backup success!"

def SqlBackup(dbuser,dbhost,dbpwd,db,gamename,gameid,custid,backfile):
    if os.path.isfile(backfile):
       logging.debug(gamename+":already backup!")
    else:
       game_game = "mysqldump -u%s -h%s -p%s %s game_game --where='id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,gameid,backfile)
       subprocess.Popen(game_game,stdout=subprocess.PIPE,shell=True)

       game_customize_common_conf = "mysqldump -u%s -h%s -p%s %s game_customize_common_conf --where='game_id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,gameid,backfile)
       subprocess.Popen(game_customize_common_conf,stdout=subprocess.PIPE,shell=True)

       game_customize = "mysqldump -u%s -h%s -p%s %s game_customize --where='game_id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,gameid,backfile)
       subprocess.Popen(game_customize,stdout=subprocess.PIPE,shell=True)

       game_customize_rank_conf = "mysqldump -u%s -h%s -p%s %s game_customize_rank_conf --where='game_id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,gameid,backfile)
       subprocess.Popen(game_customize_rank_conf,stdout=subprocess.PIPE,shell=True)

       game_customize_reward_conf = "mysqldump -u%s -h%s -p%s %s game_customize_reward_conf --where='game_id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,gameid,backfile)
       subprocess.Popen(game_customize_reward_conf,stdout=subprocess.PIPE,shell=True)

       game_customize_details = "mysqldump -u%s -h%s -p%s %s game_customize_details --where='cust_id=%s' -t --skip-lock-tables >> %s" % (dbuser,dbhost,dbpwd,db,custid,backfile)
       subprocess.Popen(game_customize_details,stdout=subprocess.PIPE,shell=True)

if __name__ == "__main__":
 Done()
   