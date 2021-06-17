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

    ##创建表
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS borrowform")
    sql = 'create table borrowform(Studentno VARCHAR(15) ,ISBN VARCHAR(20),Borrowtime DATE ,Deadline DATE);'
    cur.execute(sql)
    print("表创建成功")

except pymysql.Error as e:
    print('connect error'+str(e))




