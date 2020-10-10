import pandas as pd
import timeit as tit

#dataframe  loc,iloc,at 性能比较 : 执行10万次 分别为 2.6, 1.1, 0.6

#服务器BMS
material_details = pd.read_csv('../data/material_35w.csv')
print("记录数:", material_details['customer_id'].count())

def test1():
    value1= material_details['customer_id'].loc[100]
def test2():
    value2= material_details['customer_id'].iloc[100]
def test3():
    value3= material_details.at[100,'customer_id']

print(tit.timeit('test1()',setup='from __main__ import test1',number=100000))
print(tit.timeit('test2()',setup='from __main__ import test2',number=100000))
print(tit.timeit('test3()',setup='from __main__ import test3',number=100000))