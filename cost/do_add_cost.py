import pandas as pd

# 缺少增值对应工时

#获取增值服务列表
def get_add_detail(bms,month, customer_id):
  sql = ''' select bill_month, warehouse_code, warehouse_name,
    customer_id,customer_name,first_subject_code, 
    first_subject_name, charge_num, charge_unit
    from fees_storage_add
    where bill_month = "{}"
    and  customer_id = "{}"
    and del_flag = 0  '''.format(month,customer_id)
  add_details = pd.read_sql_query(sql, bms)
  return add_details

def do_cost(bms,month, customer_id,customer_name):
    des = '增值服务费'
    #增值服务明细
    add_details = get_add_detail(bms,month,customer_id)
    #取单小时操作成本
    prices= pd.read_excel('./data/set_operation_price.xlsx')

    #增加计算列
    add_details['optime'] = 2  #工时
    add_details['price'] = 5   #工时单价
    add_details['cost'] = 0    #工时成本

    print("开始计算！")

    # 循环行处理 （计算并更新成本）
    for i in range(len(add_details)):
        warehouse = add_details.iloc[i]['warehouse_code']
        # 单价筛选
        row = prices.loc[(prices.warehouse_id == warehouse) & (prices.month == 5)]
        price = 0
        if len(row)!=0:
           price = row['time_price'].iloc[0]
        cost = add_details.iloc[i]['optime'] * price
        # 更新工时单价和工时成本
        add_details.iloc[i,-1] = cost
        add_details.iloc[i,-2] = price

    #保存数据
    add_details.to_excel('./out/'+customer_name+'_'+des+'_'+month+'.xlsx',index=None)

    print("计算完成！")