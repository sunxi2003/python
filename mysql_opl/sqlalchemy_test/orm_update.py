# ORM更新数据
# 根据之前原有的经验,接下来是不是要导入ORM对象了,是不是要创建db_session会话了
from my_create_table import User,engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# UPDATE user SET name="NBDragon" WHERE id=20 更新一条数据
# 语法是这样的 :
# 使用 db_session 执行User表 query(User) 筛选 User.id = 20 的数据 filter(User.id == 20)
# 将name字段的值改为NBDragon update({"name":"NBDragon"})
res = db_session.query(User).filter(User.id == 20).update({"name":"NBDragon"})
print(res) # 1 res就是我们当前这句更新语句所更新的行数
# 注意注意注意
# 这里一定要将db_session中的执行语句进行提交,因为你这是要对数据中的数据进行操作
# 数据库中 增 改 删 都是操作,也就是说执行以上三种操作的时候一定要commit
db_session.commit()
db_session.close()
#关闭会话

# 更新多条
res = db_session.query(User).filter(User.id <= 20).update({"name":"NBDragon"})
print(res) # 6 res就是我们当前这句更新语句所更新的行数
db_session.commit()
db_session.close()
#关闭会话