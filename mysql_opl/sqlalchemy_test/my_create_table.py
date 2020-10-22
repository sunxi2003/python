
# 创建数据表 - 创建Object

# 导入官宣基础模型（SQLAlchemy）
from sqlalchemy.ext.declarative import declarative_base
# 实例化官宣模型 - Base 就是 ORM 模型
Base = declarative_base()

class User(Base):  
    # 为Table创建名称
    __tablename__ = "user"
    from sqlalchemy import Column,Integer,String
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32),index=True)


from sqlalchemy import create_engine
# 创建的数据库引擎
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/tmp?charset=utf8")

Base.metadata.create_all(engine)