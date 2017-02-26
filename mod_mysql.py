from MyPackage import pymysql


try:
    #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn=pymysql.connect(host='25.17.1.59',user='app_gameplatform',passwd='pFBLbBvoK1STd2IinECs3w==',db='db_wlt_gameplatform',port=3306,charset='utf8')
    cur=conn.cursor()#获取一个游标
    cur.execute('select * from game_customize_interaction_biji_details')
    data=cur.fetchall()
    print(data)
    cur.close()#关闭游标
    conn.close()#释放数据库资源
except  Exception :print("发生异常")

