import pandas as pd
import datetime as dt

#获取客户存储托盘数量
def get_storage_pallet(bms, month, customer_id):
  sql = ''' select cur_time, bill_month, warehouse_code,warehouse_name, 
                   temperature_type_code, temperature_type_name,charge_num
              from fees_storage_pallet
             where subject_name = '商品存储费'
               and bill_month = "{}"
               and customer_id = "{}"
               and del_flag = 0
               and charge_num > 0 
          order by cur_time '''.format(month,customer_id)
  pallets = pd.read_sql_query(sql, bms)
  return pallets

def do_cost(bms,month, customer_id,customer_name):
    des = '商品存储费'
    print("开始取数据:", dt.datetime.now())
    #取托盘数
    pallets = get_storage_pallet(bms, month, customer_id)
    print("记录数:", pallets['cur_time'].count())
    #取托盘单价
    plt_prices= pd.read_excel('./data/set_pallet_price.xlsx')
    print("取数据完成：", dt.datetime.now())

    #增加计算列
    pallets['price'] = 5.0
    pallets['cost'] = 0.0

    print("开始计算！",dt.datetime.now())

    # 循环行处理 （计算并更新成本）
    for index, row in pallets.iterrows():
        warehouse = row['warehouse_code']
        temperature = row['temperature_type_code']
        # 报价筛选
        var = plt_prices.loc[(plt_prices.warehouse_id == warehouse) & (plt_prices.month == 5)]
        price = 0.0
        if len(var)!=0:
             if (temperature == 'LD') or (temperature == 'LC') :
                price = var['freezer_price'].iloc[0]
             else:
                price = var['normal_price'].iloc[0]
        cost = row['charge_num'] * price
        # 更新成本单价和成本
        pallets.at[index,'price'] = price
        pallets.at[index,'cost'] = cost

    # 保存数据 index=None 不保存行索引
    pallets.to_excel('./out/'+customer_name+'_'+des+'_'+month+'.xlsx',index=None)

    print("计算完成！",dt.datetime.now())