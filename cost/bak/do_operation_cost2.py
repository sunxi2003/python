import the_pandas as pd
from sqlalchemy import create_engine
import datetime as dt

#订单操作费：每单操作工时641秒

#服务器BMS
engine=create_engine('mysql+pymysql://bms_prd_zt_ls:bms_prd_zt-tmp@345@172.20.22.44:3306/bmssite_prd')

#获取订单列表
def get_orders(month,customer_id):
 sql = '''select bill_month,customer_id, customer_name, warehouse_code,warehouse_name,
          outstock_no,waybill_no, total_qty, total_sku_num ,total_weight
   from fees_storage_outstock
  where bill_month = "{}"
    and customer_id = "{}" 
    and del_flag = 0 '''.format(month,customer_id)
 orders = pd.read_sql_query(sql, engine)
 return orders

#本地数据库
engine2=create_engine('mysql+pymysql://root:''@localhost:3306/bms_cost')

#获取单小时操作成本
def get_operation_price():
  return pd.read_sql_query('select  * from set_operation_price', engine2)

print("开始取数据:",dt.datetime.now())
#取订单列表
orders = get_orders('202005','1100001514')
print("记录数:", orders['outstock_no'].count())

#取单小时成本
prices = get_operation_price()
print("取数据完成：",dt.datetime.now())

#增加计算列
orders['time'] = 641  #订单工时
orders['price'] = 0   #工时成本
orders['cost'] = 0    #行成本

print("开始计算！",dt.datetime.now())

# 循环行处理 （计算并更新成本）
for i in range(len(orders)):
    warehouse = orders.iloc[i]['warehouse_code']
    # 工时成本筛选
    price = 0
    var = prices.loc[(prices.warehouse_id == warehouse) & (prices.month == 5)]
    if len(var)!=0:
        price = var['time_price'].iloc[0]
    # 成本
    cost = 641 * price/3600

    # 更新工时和成本
    orders.iloc[i,-1] = cost
    orders.iloc[i,-2] = price

print("计算完成！", dt.datetime.now())

print("保存数据：",dt.datetime.now())
#保存到数据库表& out  index=None 不保存行索引
orders.to_sql('cost_operation2', engine2, index=None)
# orders.to_csv('./out/cost_operation2.out',index=None)

print("保存完成！",dt.datetime.now())











