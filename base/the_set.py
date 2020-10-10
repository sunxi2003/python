'''set是一组key的集合
在set中，没有重复的key
set和dict的唯一区别仅在于没有存储对应的value '''
s1 = set([1, 1, 2, 2, 3, 3])
print("s1=",s1)
s2 = set([2, 3, 4, 4])
print("s2=",s2)

# 求交集
print("s1 & s2 = ",s1 & s2)
# 求并集
print("s1 | s2 = ", s1 | s2)

#添加元素到set中
s1.add(5)
print(s1)

#删除元素
s1.remove(5)
print(s1)

s99 = set(["zs", "ls","ww","wc"])
s99.add("sunxi")
s99.remove("ww")
print(s99)

