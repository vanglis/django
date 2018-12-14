#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W

import configparser
import os

def getConfig(section):
	config = configparser.ConfigParser()
	filepath = os.path.split(os.path.realpath(__file__))[0]+'/config.conf'
	config.read(filepath)
	cf =  config.items(section)
	cfg = {}
	for k,v in cf:
		cfg[k]=v
	return cfg
