# coding : utf-8
# 夏目&青一
# @name:04_查询数据
# @time: 2023/6/9  23:55
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='xiamu',
                     database='test')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
sql1 = "SELECT * FROM EMPLOYEE "
try:
    # 执行SQL语句
    cursor.execute(sql1)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
