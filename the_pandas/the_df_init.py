import pandas as pd

# 创建dataframe

#定义一个tuple: 使用"（）"小括号定义,不能修改
names = ('zhangsan', 'lisi', 'wangwu','Kevin')
print(names[0])

#定义一个list: 使用"[]"中括号定义
list2 = ['zhangsan', 'lisi', 'wangwu','Kevin']
print(list2[0])

#定义一个Dict: 使用"{}"大括号定义
classmates ={'Michael': 95, 'Bob': 75,'Tracy': 85}
print(classmates['Bob'])

#定义一个set: set是一组key的集合,没有重复
s1 = set([1, 1, 2, 2, 3, 3])
print("s1=",s1)

# 1. 定义DataFrame（通过dict）
data1= {'name':['张三','李四','王五'],
        'age':[17,18,19],
        'height':[165,170,180]}
students = pd.DataFrame(data1)
print(students)

# 2. 定义DataFrame（通过dict）
data2 = {'name':list('abcde'),'age':range(5)}
df1 = pd.DataFrame(data2)
print(df1)