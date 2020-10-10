'''
字典 dict
使用"{}"(大括号)定义
'''

#定义字典
d={'Michael': 95, 'Bob': 75,'Tracy': 85}

# 检查是否包含1：返回true/false
print('Bob' in d)

# 检查是否包含2： 不存在时返回 None
print(d.get('Bob2'))

# 获取值
s= d['Bob']
print(s)

# 设置值 (会覆盖现有的值)
d['Bob'] = 99
print(d['Bob'])

# 删除一个key
d.pop('Bob')
print(d)

'''
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
'''
