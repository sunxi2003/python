from pymysql_utrl import MySQL

mysql=MySQL('127.0.0.1','root','root','tmp')

# 新增
from faker import Faker     #随机函数库
fk = Faker(locale='zh_CN')
insert_sql = 'insert into user (id, name) values ("{}", "{}")'.format(fk.random_int(), fk.name())
result = mysql.exe_sql(insert_sql); 
print("新增行数: ", result)

# 删除
delete_sql = "delete from user where id < 500 ;"
delete_result = mysql.exe_sql(delete_sql); 
print("删除行数: ", delete_result)

# 修改
update_sql = "update user set name = '张三' where id = 4310 ;"
update_result = mysql.exe_sql(update_sql); 
print("修改行数: ", update_result)

# 查询
query_sql='select * from user order by id desc ;'
users= mysql.get_all(query_sql)
print(users[0])









