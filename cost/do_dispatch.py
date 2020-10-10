import pandas as pd

# 用系统单据匹配线下账单（merge）

# 获取线上运单
def get_dispatch_detail(bms,month, customer_id):
  sql = '''select  bill_month, outstock_no, waybill_no, external_no,customer_id,
        customer_name,warehouse_code,warehouse_name, 
				carrier_id,carrier_name, charge_weight
          from  fees_dispatch
        where  bill_month = "{}"
        and customer_id = "{}"
        and del_flag = 0  '''.format(month,customer_id)
  dispatch_details = pd.read_sql_query(sql, bms)
  return dispatch_details

# 数据匹配
def do_cost(bms,month, customer_id,customer_name):
    des = '宅配配送费'

    #读取线上数据（5月应收）
    online_datas = get_dispatch_detail(bms,month,customer_id)
    print('系统行数：', len(online_datas))

    #读5月份线下账单
    m5_datas = pd.read_excel('data/宅配应付2020-05.xlsx')
    print('账单行数：', len(m5_datas))

    # 用运单号匹配 使用isin
    orders = online_datas['waybill_no'].to_list();
    results = m5_datas.loc[m5_datas['运单号'].isin(orders)]
    print('匹配行数：', len(results))

    #保存
    results.to_excel('./out/'+customer_name+'_'+des+'_'+month+'.xlsx',index=None)