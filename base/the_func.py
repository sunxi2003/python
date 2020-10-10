#定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x;

'''在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。'''

print(my_abs(-55))

#默认参数使用
def student(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#使用默认参数
student("张三","男","18");

#给默认参数命名
student("lisi","女","18","上海");

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3));  # 1+4+9 = 14

#递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5));  #计算5的阶乘