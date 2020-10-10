''' 元祖
tuple一旦初始化就不能修改    (使用"（）"小括号定义)
在定义的时候，tuple的元素就必须被确定下来'''

#定义一个tuple
t = (1, 2)
print(t)

#获取元素
print(t[1])

#样例:多维数组
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])