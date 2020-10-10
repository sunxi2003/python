import the_pandas as pd
from sqlalchemy import create_engine

#订单操作费：按订单明细品类工时合计 * 工时成本计算
#缺少品类操作工时

#服务器BMS
engine=create_engine('mysql+pymysql://omsprd_read:Oms123456@172.20.22.40:3306/omsprd')

#获取订单明细
def get_order_detail():
 sql = '''select  cus.customerid, cus.customername,  w.warehouseid, w.warehousename, 
a.orderno, a.productid, a.productname, a.qty, p.categoryid, c.categoryname  
from oms_orderinfoitem a
join oms_orderinfo b on a.orderno = b.orderno
join pub_product p on a.productid = p.productid
join pub_productcategory  c on p.categoryid =c.categoryid 
join pub_customer cus on b.customerid = cus.customerid
join pub_warehouse w on b.originwarehouseid = w.warehouseid
where b.customerid = '1100001514'
and a.cre_time > '2020-04-21'
and a.cre_time < '2020-05-20'
and b.exceptionflag = 0 
limit 100 '''
 orders = pd.read_sql_query(sql, engine)
 return orders

#本地数据库
engine2=create_engine('mysql+pymysql://root:''@localhost:3306/bms_cost')

#取品类操作标准时长
def get_category_time():
  return pd.read_sql_query('select * from set_category_time', engine2)

#取单小时操作成本
def get_operation_price():
  return pd.read_sql_query('select  * from set_operation_price', engine2)

#取订单明细
orders = get_order_detail();
print("orders:", orders.count())

#取品类操作时长
times = get_category_time()

#取单小时成本
prices = get_operation_price()

#增加计算列
orders['time'] = 0  #品类时间
orders['price'] = 0 #工时成本
orders['cost'] = 0  #行成本

print("开始计算！")

# 循环行处理 （计算并更新成本）
for i in range(len(orders)):
    warehouse = orders.iloc[i]['warehouseid']
    # 报价筛选
    time = 0
    row = times.loc[(times.warehouse_id == warehouse) & (times.month == 5)]
    if len(row)!=0:
        time = row['task_time'].iloc[0]
    # 工时成本筛选
    price = 0
    var = prices.loc[(prices.warehouse_id == warehouse) & (prices.month == 5)]
    if len(var)!=0:
        price = var['time_price'].iloc[0]
    # 数量
    qty = orders.iloc[i]['qty']
    # 成本
    cost = qty*time * price/3600

    # 更新工时和成本
    orders.iloc[i,-1] = cost
    orders.iloc[i,-2] = price
    orders.iloc[i,-3] = time

#保存到数据库表& out  index=None 不保存行索引
orders.to_sql('cost_operation', engine2, index=None)
orders.to_csv('./out/cost_operation.out',index=None)

print("计算完成！")











