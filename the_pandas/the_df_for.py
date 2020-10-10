import pandas as pd
from sqlalchemy import create_engine
import datetime as dt

#dataframe 循环遍历

#服务器BMS
material_details = pd.read_csv('../data/material_35w.csv')
print("记录数:", material_details['customer_id'].count())

print("开始计算:", dt.datetime.now())
# 循环行处理 （计算并更新成本）
for index,row in material_details.iterrows():
    warehouse = row['warehouse_code']
    material = row['consumer_material_code']
    # row['cost'] = 100   修改无效
    # material_details.iloc[index, -1] = cost  修改有效
print("计算完成:",dt.datetime.now())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("开始计算:",dt.datetime.now())
# 循环行处理 （计算并更新成本）
for i in range(len(material_details)):
    warehouse = material_details.iloc[i]['warehouse_code']
    material = material_details.iloc[i]['consumer_material_code']
print("计算完成:",dt.datetime.now())

