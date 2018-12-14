#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-04-11
Author: xiaohanfei
TODO: 切换分支
'''
import sys,os
import subprocess
import logging

logging.basicConfig(  
   level = logging.DEBUG, #将来布署到生产环境之后就修改成error级别了
   format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',  
   filename = '/home/www/django.log',  #日志存放的目录
)

def php_checkout(branchname,game_dir):
 dir = game_dir
 os.chdir(dir)
 output1 = subprocess.getoutput('git fetch')
 output2 = subprocess.getoutput('git checkout -- .')
 output3 = subprocess.getoutput('git checkout '+branchname)
 output4 = subprocess.getoutput('git pull')
 logging.debug(output1)
 logging.debug(output2)
 logging.debug(output3)
 logging.debug(output4)

if __name__ == "__main__":
    branchname = sys.argv[1]
    game_dir = sys.argv[2]
    r = php_checkout(branchname,game_dir)
