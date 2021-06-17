# -*- coding = utf-8 -*-
# @time : 2021/6/16 20:01
# @Author : wgys
# @File : 表中插入数据.py
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

    ##插入数据到表
    cur = db.cursor()
    sql = 'INSERT INTO borrowform values (%s,%s,%s,%s)'
    value = ('201915365824', '9787508689586', '2021/5/12', '2021/5/15')
    cur.execute(sql, value)
    db.commit()
    print("数据插入成功")

except pymysql.Error as e:
    print('connect error'+str(e))





