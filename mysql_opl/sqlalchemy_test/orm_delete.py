# ORM 删除一条多条数据
# 导入 ORM 创建会话
from my_create_table import User,engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# DELETE FROM `user` WHERE id=6
res = db_session.query(User).filter(User.id==6).delete()
print(res)
db_session.commit()

db_session.close()
#关闭会话