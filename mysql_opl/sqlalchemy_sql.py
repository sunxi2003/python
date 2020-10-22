# sqlalchemy执行SQL语句
# 参考： https://www.cnblogs.com/richiewlq/p/8269135.html

from sqlalchemy import create_engine

# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/tmp")
  
# 查询多条数据
def get_all(sql):
    cur = engine.execute(sql)
    result = cur.fetchall()
    cur.close()
    return result

# 查询单条数据
def get_one(sql):
    cur = engine.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result   

 # 执行增删改
def exe_sql(sql):
    cur = engine.execute(sql)
    cur.close()
    
# 查询测试
sql = "select * from user"
result = get_all(sql)
print(result)

# 修改测试
sql2 = "update user set name = '张三' where id = 1 ;"
exe_sql(sql2)




