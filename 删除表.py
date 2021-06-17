# -*- coding = utf-8 -*-
# @time : 2021/6/17 8:35
# @Author : wgys
# @File : 删除表.py
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
    sql = "drop table if exists adminform"
    cur.execute(sql)
    print("表删除成功")

except pymysql.Error as e:
    print('表删除失败'+str(e))
    db.rollback()

db.close()