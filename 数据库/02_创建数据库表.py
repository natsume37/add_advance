import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='xiamu',
                     database='test')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE repider (
         auther  CHAR(20) NOT NULL,
         NAME  CHAR(20),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()