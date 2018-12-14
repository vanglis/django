import pymysql

conn = pymysql.connect(host='25.17.1.59',port=3306,user='app_gameplatform',passwd='game12345',db='db_wlt_gameplatform')
cur = conn.cursor()
a = cur.execute("SELECT * FROM game_customize_user_account WHERE user_id=2037593400;")
print (a)
cur = [x for x in cur]
print (cur)
print(type(a))
cur.close()
conn.close()

