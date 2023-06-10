# coding : utf-8
# 夏目&青一
# @name:插入数据
# @time: 2023/6/9  23:52

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='xiamu',
                     database='test')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(auther,
         name,INCOME)
         VALUES ('张占士', '六六六', 1000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()