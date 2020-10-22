from orm_create_table import User,engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# 更新单条
res = db_session.query(User).filter(User.id == 10).update({"name":"张三"})
print(res) 
db_session.commit()
db_session.close()


# 更新多条
res = db_session.query(User).filter(User.id <= 3).update({"name":"张三"})
print(res) 
db_session.commit()
db_session.close()
