import pandas as pd
import datetime as dt

#订单操作费： 订单工时 = 基础工时（1件） + 增量工时 ；

#获取订单列表
def get_orders(bms,month,customer_id):
 sql = '''select bill_month,customer_id, customer_name, warehouse_code,warehouse_name,
          outstock_no,waybill_no, total_qty, total_sku_num ,total_weight
   from fees_storage_outstock
  where bill_month = "{}"
    and customer_id = "{}" 
    and del_flag = 0 '''.format(month,customer_id)
 orders = pd.read_sql_query(sql, bms)
 return orders

def do_cost(bms,month, customer_id,customer_name):
    des = '订单操作费'
    print("开始取数据:",dt.datetime.now())
    #取订单列表
    orders = get_orders(bms,month, customer_id)
    print("记录数:", orders['outstock_no'].count())

    #取单小时成本
    prices = pd.read_excel('./data/set_operation_price.xlsx')
    print("取数据完成：",dt.datetime.now())

    #增加计算列
    orders['order_time'] = 0.00    #订单工时
    orders['price'] = 0.00    #工时成本
    orders['cost'] = 0.00     #行成本

    print("开始计算！",dt.datetime.now())

    # 循环行处理 （计算并更新成本）
    for index,row in orders.iterrows():
        warehouse = row['warehouse_code']
        qty = row['total_qty']

        # 工时成本
        price = 26.00
        var = prices.loc[(prices.warehouse_id == warehouse) & (prices.month == 5)]
        if len(var)!=0:
            price = var['time_price'].iloc[0]

        # 单件工时 办公室分摊8%
        single_time = 40.00

        # 订单总工时
        order_time = 400
        if qty>3:
            order_time = 400 + (qty-3)* single_time

        # 成本 = 订单工时 *  工时单价 + 0.5 （操作区仓租费分摊）
        cost = order_time * price/3600

        # 更新工时和成本
        orders.at[index,'cost'] = cost
        orders.at[index,'order_time'] = order_time
        orders.at[index,'price'] = price

    print("计算完成！", dt.datetime.now())

    print("保存数据：",dt.datetime.now())

    #保存数据
    orders.to_excel('./out/'+customer_name+'_'+des+'_'+month+'.xlsx',index=None)

    print("保存完成！",dt.datetime.now())











