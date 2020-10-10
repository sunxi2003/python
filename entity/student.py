from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class News(Base):
  # 表名称
  __tablename__ = 'news'
  # news表里id字段
  id = Column(Integer, primary_key=True, autoincrement=True)
  # news表里title字段
  title = Column(String(length=255), nullable=False)
  # news表里title字段
  content = Column(String(length=255), nullable=False)