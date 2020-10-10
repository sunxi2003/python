import pandas as pd
from sqlalchemy import create_engine

# 定义DataFrame
data1= {'name':['张三','李四','王五'],
        'age':[17,18,19],
        'tall':[165,170,180]}
students = pd.DataFrame(data1);
print("1: students \n ", students)

# 取某一列
ages =students['age'];
print("2: ages: \n",ages )

# 取某一行
row2 = students.loc[2];
print("3: row2: \n",row2)

# 取某一单元格
var = students.iloc[1,1];
print("4：var: \n",var)

# 按条件筛选
lisi = students.loc[(students.name == '李四') & (students.age == 18)]
print("5：lisi: \n",lisi)
print("6：lisi.name: \n",lisi['name'].iloc[0])  #取结果中的值

# 增加列
students['gender'] = '男'
print("7: students \n",students)

# 增加行
students.loc[3] =['国强',35,178,"男"]
print("8: students \n",students)

# 删除列
del students['gender']
print("9: students \n",students)

# 删除行
students.drop([3] ,inplace=True)
print("10: students \n",students)

#保存到CSV index=None 不保存行索引
students.to_csv('student.out',index=None)

#读取CSV
stu = pd.read_csv('student.csv')
print("11: 记录数：\n",stu['name'].count())

# 保存到数据库
engine=create_engine('mysql+pymysql://root:''@localhost:3306/tmp')
# students.to_sql('students', engine, index=None，if_exists='replace')

# to_sql() 方法的 if_exists 参数用于当目标表已经存在时的处理方式，
# 默认是 fail：即目标表存在就失败；
#       replace ： 表示替代原表，即删除再创建；
#       append ： 选项仅添加数据 ；

'''DataFrame这种数据结构我们可以把它看作是一张二维表，DataFrame长得跟我们平时使用的Excel表格差不多，
DataFrame的横行称为columns，竖列和Series一样称为index，
DataFrame每一列可以是不同类型的值集合，
所以DataFrame你也可以把它视为不同数据类型同一index的Series集合。
https://www.cnblogs.com/peng104/p/10398490.html '''

# 遍历: 使用iterrows
for index,row in students.iterrows():
    name = row['name']
    print("name:",name)

# 遍历：
for i in range(len(students)):
    name = students.iloc[i]['name']
    print("name:", name)