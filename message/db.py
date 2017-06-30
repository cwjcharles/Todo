# -*- coding:utf-8 -*-
import MySQLdb
conn=MySQLdb.connect('127.0.0.1', 'root','charles2009', 'test')
cur = conn.cursor()
def addUser(username,password):
    sql='insert into user(username,password) values("%s","%s")'%(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()
def isExisted(username,password):
    sql="select * from user where username='%s' and password='%s'"%(username,password)
    cur.execute(sql)
    result=cur.fetchall()
    if (len(result))==0:
        return False
    else:
        return True
