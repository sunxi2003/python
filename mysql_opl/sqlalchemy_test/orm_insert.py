#insert 为数据表增加数据

# 1.首先导入之间做好的ORM 对象 User
from my_create_table import User
# 2.使用Users ORM模型创建一条数据
user1 = User(name="wang")

# 导入 sqlalchemy.orm 中的 sessionmaker
from sqlalchemy.orm import sessionmaker
# 导入之前创建好的 create_engine
from my_create_table import engine
# 创建 sessionmaker 会话对象,将数据库引擎 engine 交给 sessionmaker
Session = sessionmaker(engine)
# 打开会话对象 Session
db_session = Session()
# 在db_session会话中添加一条 UserORM模型创建的数据
db_session.add(user1)
# 使用 db_session 会话提交 , 这里的提交是指将db_session中的所有指令一次性提交
db_session.commit()

# 当然也你也可很任性的提交多条数据
# 方法一:
user2 = User(name="张三")
user3 = User(name="王五")
db_session.add(user2)
db_session.add(user3)
db_session.commit()
# 之前说过commit是将db_session中的所有指令一次性提交,现在的db_session中至少有两条指令user2和user3
db_session.close()
#关闭会话

# 方法二:
user_list = [
    User(name="wang1"),
    User(name="wang2"),
    User(name="wang3")
]
db_session.add_all(user_list)
db_session.commit()

db_session.close()
