#/usr/bin/env python
# _*_ conding:utf-8 _*_

import psycopg2
Con = psycopg2.connect(host='10.35.53.55',user='app_gameplatform',password='app_gameplatform123',port='3306',db='game')
cur = con.cursor()
cur.execute(sql = "select * from game_user where id='30000129';")
for row in cur:
print (row[0])
conn.close()





