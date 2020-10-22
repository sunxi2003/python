from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# 实例化ORM模型
Base = declarative_base()

class User(Base):  
    __tablename__ = "user"
    from sqlalchemy import Column,Integer,String
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32),index=True)

# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/tmp")

Base.metadata.create_all(engine)