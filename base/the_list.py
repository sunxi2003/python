''' 列表
    一种有序的集合，可以随时添加和删除其中的元素
    注： (使用 "[]"中括号定义) '''
# 例
classmates = ['Michael', 'Bob', 'Tracy','Kevin']
#获取元素（第一个）
print(classmates[0])
# 获取元素（最后一个）
print(classmates[-1])
# 添加元素
classmates.insert(0,"zhangsan")
print(classmates)
# 移除元素
classmates.pop(0)
print(classmates)
# 移除元素（最后一个）
classmates.pop(-1)
print(classmates)
# 修改元素
classmates[0] = "lisi"
print(classmates)
#排序
classmates.sort()
print(classmates)