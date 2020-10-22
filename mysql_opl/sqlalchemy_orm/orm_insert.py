from orm_create_table import User
from sqlalchemy.orm import sessionmaker
from orm_create_table import engine

# ======= 为数据表增加数据 ========

# 新增
user1 = User(name="wang")
Session = sessionmaker(engine)
db_session = Session()
db_session.add(user1)
db_session.commit()

# 提交多条数据：方法一
user2 = User(name="张三")
user3 = User(name="王五")
db_session.add(user2)
db_session.add(user3)
db_session.commit()
db_session.close()

# 提交多条数据：方法二
user_list = [
    User(name="wang1"),
    User(name="wang2"),
    User(name="wang3")
]
db_session.add_all(user_list)
db_session.commit()
db_session.close()
