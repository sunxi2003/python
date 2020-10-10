import pandas as pd
# 参考资料  https://blog.csdn.net/Asher117/article/details/84725199


# 1. 按相同列名匹配  on='name'
df1 = pd.DataFrame({'name':list('abcde'),'age':range(5)});
print(df1)

df2 = pd.DataFrame({'name':list('abcde'),'score':range(5)});
print(df2)

df3 = pd.merge(df1,df2,on='name')
print(df3)

# 2. 按指定列名合并 left_on='name',right_on='id'
df11 = pd.DataFrame({'name':list('abcde'),'age':range(5)});
print(df1)

df22 = pd.DataFrame({'id':list('abcde'),'score':range(5)});
print(df2)

df33 = pd.merge(df11,df22,left_on='name',right_on='id')
print(df33)

# 排序并取前几条
result = df33.sort_values(["score"],ascending=False).head(3)
print(result)
