# -*- coding = utf-8 -*-
# @time : 2021/6/16 20:31
# @Author : wgys
# @File : 查询表中数据.py
# @Software : PyCharm
import pymysql

try:
    ##连接数据库
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='library_management_system',
        charset='utf8'
    )
    print('mysql connect success')

    ##查询表中数据
    cur = db.cursor()
    sql = 'SELECT * FROM book'
    cur.execute(sql)
    results= cur.fetchall()
    for row in results:
        ISBN = row[0]
        Bookname = row[1]
        Author = row[2]
        print('ISBN:%s,书名:%s,作者:%s'%(ISBN, Bookname, Author))
    print("数据查询成功")

except pymysql.Error as e:
    print('connect error'+str(e))

db.close()