import time
import datetime as dt

#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=8, tm_hour=13, tm_min=56, tm_sec=48, tm_wday=2, tm_yday=190, tm_isdst
print(time.localtime());

#当前时间戳  1594187863.2898781
print(time.time());

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

#https://www.runoob.com/python/python-date-time.html

#这个更好用  2020-07-08 18:52:38.949209
print(dt.datetime.now())