# -*- coding = utf-8 -*-
# @time : 2021/6/17 8:31
# @Author : wgys
# @File : 删除表中数据.py
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

    ##删除表中数据
    cur = db.cursor()
    sql = "delete from borrower where Studentname=%s"
    value = ('王水悦')
    cur.execute(sql, value)
    db.commit()
    print("数据删除成功")

except pymysql.Error as e:
    print('数据删除失败'+str(e))
    db.rollback()

db.close()