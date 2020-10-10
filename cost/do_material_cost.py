import pandas as pd
import datetime as dt
from sqlalchemy import create_engine

#获取耗材列表


def get_material_detail(bms,month, customer_id):
  sql = '''select customer_id, customer_name, outstock_no,waybill_no, warehouse_code, 
      warehouse_name, consumer_material_code,  
      consumer_material_name, 
      case consumer_material_code  
			 when 'JY-GB' then total_weight  
			 when 'JY-GB500' then total_weight 
			 else total_qty 
			 end 'charge_num'
    from fees_storage_material 
    where bill_month = "{}"
    and customer_id = "{}" 
    and del_flag = 0 '''.format(month,customer_id)
  material_details = pd.read_sql_query(sql, bms)
  return material_details

def do_cost(bms,month, customer_id,customer_name):
    des = '耗材使用费'
    print("开始取数据:",dt.datetime.now())
    #耗材使用明细
    material_details = get_material_detail(bms, month, customer_id)
    print("记录数:", material_details['customer_id'].count())
    #用量标准
    stands= pd.read_excel('./data/set_material_stand.xlsx')
    #成本价
    prices= pd.read_excel('./data/set_material_price.xlsx')
    print("取数据完成:",dt.datetime.now())

    #增加计算列
    material_details['price'] = 0.00   #单价
    material_details['stand'] = 1.00   #用量标准
    material_details['cost'] = 0.00    #成本

    print("开始计算:",dt.datetime.now())

    # 循环行处理 （计算并更新成本）
    for index,row in material_details.iterrows():
        warehouse = row['warehouse_code']
        material = row['consumer_material_code']
        # 单价匹配
        price = 0.00
        results = prices.loc[(prices.warehouse_id == warehouse) & (prices.month == 5) &(prices.material_id == material)]
        if len(results)!=0:
           price = results['price'].iloc[0]
        # 用量标准匹配
        stand = 1.00
        var = stands.loc[(stands.warehouse_id == warehouse) & (stands.month == 5) &(stands.material_id == material)]
        if len(var)!=0:
            stand = var['qty'].iloc[0]
        # 行成本
        cost = row['charge_num'] * stand * price
        # 更新工时单价和工时成本
        material_details.at[index,'price'] = price
        material_details.at[index,'stand'] = stand
        material_details.at[index,'cost'] = cost

    print("计算完成:",dt.datetime.now())

    print("保存数据:",dt.datetime.now())
    #保存到数据库表&out index=None 不保存行索引
    local = create_engine('mysql+pymysql://root:''@localhost:3306/bms_cost')
    material_details.to_sql('cost_material_'+customer_id+'_'+month, local, index=None,if_exists='replace')
    material_details.to_excel('./out/'+customer_name+'_'+des+'_'+month+'.xlsx',index=None)

    print("保存完成！")