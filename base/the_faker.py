from faker import Faker

#初始化
fk = Faker(locale='zh_CN')

names = fk.name()
print(names)

add = fk.address()
print(add)

for i in range(100):
  print(fk.name())

print(Faker().random_int())
