import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接
engine=create_engine('mysql+pymysql://root:''@localhost:3306/tmp')
sql = ' select * from user; '
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)
# 输出employee表的查询结果
print(df)

# 新建DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# 保存到MySQL表，index=True：储存index列
df.to_sql('mydf', engine, index=True) #mydf表名， engine：存到相应的数据库下面
print('操作成功!')