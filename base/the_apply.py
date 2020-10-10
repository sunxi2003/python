import the_pandas as pd
from sqlalchemy import create_engine
import time
#dataframe 遍历

#服务器BMS
engine=create_engine('mysql+pymysql://bms_prd_zt_ls:bms_prd_zt-tmp@345@172.20.22.44:3306/bmssite_prd')

#获取耗材列表
def get_material_detail():
  sql = '''select customer_id, customer_name, outstock_no, warehouse_code, 
      warehouse_name, consumer_material_code,  
      consumer_material_name, charge_num 
    from fees_storage_material 
    where bill_month = '202005'
    and customer_id = '1100001514'
    and del_flag = 0  
    limit 3500'''
  material_details = pd.read_sql_query(sql, engine)
  return material_details

material_details = get_material_detail()

engine = create_engine('mysql+pymysql://root:''@localhost:3306/bms_cost')
prices = pd.read_sql_query('select  * from set_material_price', engine)
material_details['price'] = 0
def math_price(row):
    p=prices.loc[(prices.warehouse_id==row.warehouse_code)
                 &(prices.material_id==row.consumer_material_code)].price
    if len(p):
        row.price = p.iloc[0]
print(time.time())
material_details.apply(math_price,axis=1)
print(time.time())