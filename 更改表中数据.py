# -*- coding = utf-8 -*-
# @time : 2021/6/17 8:20
# @Author : wgys
# @File : 更改表中数据.py
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

    ##更新表中数据
    cur = db.cursor()
    sql = "update borrower set Studentname=%s where Studentname=%s"
    value = ('李华', '守谷菱')
    cur.execute(sql, value)
    db.commit()
    print("数据更新成功")

except pymysql.Error as e:
    print('数据更新失败'+str(e))
    db.rollback()

db.close()