import pandas as pd

# 1 ：通过list定义
# 未设置index值，Series自动生成index
list = [1,2,3,4]
data1 = pd.Series([1,2,3,4])
print('data1:',data1)

# 设置index
data2 = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print('data2:',data2)

# 2： 通过DIC定义
dic = {'a':1,'b':2,'c':3}
data3 = pd.Series(dic)
print(data3)

 #显示索引
data2.index
# out: Index(['a', 'b', 'c', 'd'], dtype='object')

#显示值
data2.values
#out: array([1, 2, 3, 4])



'''Series是一种类似一维数组的数据结构，由一组数据和与之相关的index组成，
这个结构一看似乎与dict字典差不多，我们知道字典是一种无序的数据结构，
而pandas中的Series的数据结构不一样，它相当于定长有序的字典，
并且它的index和value之间是独立的，两者的索引还是有区别'''