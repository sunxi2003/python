import pymysql
from faker import Faker

fk = Faker(locale='zh_CN')

conn = pymysql.connect(user='root', password='', database='tmp')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table IF NOT EXISTS user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)',
               (fk.random_int(), fk.name()))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()