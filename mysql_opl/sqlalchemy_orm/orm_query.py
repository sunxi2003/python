
from orm_create_table import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()

# 1. 查询user表中的所有数据
user_all_list = db_session.query(User).all() 
for i in user_all_list:
    print(i.id, i.name)  
db_session.close()

# 2. 带条件查询
user_all_list = db_session.query(User).filter(User.id >= 10).all()
for i in user_all_list:
    print(i.id, i.name)
db_session.close()

# 3. 只取出一条
user = db_session.query(User).filter(User.id == 5).first()
print('3:', user.id, user.name)
db_session.close()

# 4. 查看sql语句
query1 = db_session.query(User).filter(User.id >= 20)
print(query1)
query2 = db_session.query(User)
print(query2)
db_session.close()