import pandas as pd
from sqlalchemy import create_engine

#从OMS查询商家简称、联系人、电话同步到合同在线

#OMS
engine=create_engine('mysql+pymysql://omsprd_read:Oms123456@172.20.22.40:3306/omsprd')

#查询oms商家
def get_oms_customers():
  return pd.read_sql_query('select  * from pub_customer', engine)

#取OMS商家列表
oms_customers = get_oms_customers()
print("OMS记录数:", oms_customers['customerid'].count())

#==========开始更新 =============
# 合同DB 
ht_engine=create_engine('mysql+pymysql://ct_prod:ct_prod@2018@172.20.23.29:3306/contract')

# 更新
for index,row in oms_customers.iterrows():
    name = row['shortname']
    id = row['customerid']
    linkman = row['linkman']
    tel = row['tel']
    sql = 'update contract_custom_sub set short_name="{}",link_man="{}",link_man_phone="{}" where custom_sub_no = "{}" ;'.format(name,linkman,tel,id)
    print(sql)
    ht_engine.execute(sql)  #执行sql 
