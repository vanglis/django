#!/usr/bin/env python
#-*-coding:utf-8-*-
#author:PF.W


'''
本程序用于测试环境连接DB使用，屏蔽update和delete操作没有where条件等不规范语句
'''

import pymysql
from tools.config.getConfig import getConfig
import re,time,sys

def conn(mydb,sql):
	try:
		dbconfig = getConfig(mydb)
		conn = pymysql.connect(host=dbconfig['host'],user=dbconfig['user'],passwd=dbconfig['passwd'],db=dbconfig['db'],port=3306)
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute(sql.encode(encoding="utf-8"))
		conn.commit()
		result = [x for x in cur]
		cur.close()
		conn.close()
		return result
	except Exception as e:
		print ('except:%s'%e)
		main()

def reg(sql):
	reg1 = re.compile(r"(update )(.*)( set )(.*)( where )",re.I)
	reg2 = re.compile(r"(delete)(.*)( from )(.*)( where )",re.I)
	if sql.lower().find('update ')>=0 or sql.lower().find('delete ')>=0:
		if re.findall(reg1,sql) or re.findall(reg2,sql):
			return True
		else:
			return False
	else:
		return True

def main():
	sql = input('/>')
	if sql in ('q','Q'):
		sys.exit()
	open('sql.log','a').write(sql+'\n')
	if reg(sql):
		print ('\nresult:')
		start_time = time.time()
		res = conn(sql)
		for lin in res:
			for k,v in sorted(lin.items(),key=lambda d:d[0]):
				print ('\t',k,'=>',v)
			print ('---'*5)
		print ('total:%s,usedtime:%s'%(len(res),time.time()-start_time))
	else:
		print (r'请规范输入语句。。。')
	main()


if __name__ == '__main__':
	conn('db_wlt_gameplatform','SELECT SUM(add_count) AS count FROM game_activity_match_details where match_from = 1;')