from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from entity.student import News

# 连接本地test数据库
engine=create_engine('mysql+pymysql://root:''@localhost:3306/tmp')
# 创建会话
session = sessionmaker(engine)
mySession = session()

# 查询结果集（sql）
result = engine.execute("select * from news")
print(result.fetchall())

# 查询结果集
result = mySession.query(News).all()
print('记录数：',len(result))

# 新增
news = News(title="这里是标题",content="这里是内容")
mySession.add(news)
mySession.commit()
print('新增成功！')

# 查询第1条
result = mySession.query(News).first()
print('第1条：',result.title) #打印对象属性

# 根据主键查询
result = mySession.query(News).get(3)
print('id为3：',result.title)

# 查询id为2的记录
result = mySession.query(News).filter(News.id==2).first()
print('id为2：',result.title)

# 分页查询 0,2
# result = mySession.query(News).filter(News.id>1).limit(2).offset(0).all()
# print(result)

# 自定义过滤条件
result = mySession.query(News).filter(text("id>:id")).params(id=2).all()
print('记录数：',len(result))







