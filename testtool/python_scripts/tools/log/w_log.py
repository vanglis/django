#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

from datetime import datetime,time
import os
import logging

def w_log(filenames,context):
	now = datetime.now()
	filepath = '/data/httpd/python/log/%s/'%(now.strftime("%Y/%m/%d"))
	logging.basicConfig(level=logging.INFO,
	                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	                filename=filepath+filenames+'.log',
	                filemode='a')
	logging.info(context)

if __name__ == '__main__':
	w_log('1','2')
