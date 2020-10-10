from mysql.mysqlbase import MySQL

mysql=MySQL('localhost','root','zt1234567','costanalysis')

#存储费用成本计算
def storage_fee_cost_op():
    print('存储费用计算完成')
#耗材费用成本计算
def consumables_fee_cost_op():
    print('存储费用计算完成')
#运费用计算
def delivery_fee_cost_op():
    print('存储费用计算完成')
#订单操作费
def Operating_fee_cost_op():
    print('存储费用计算完成')
#增值服务费
def value_fee_cost_op():
    print('存储费用计算完成')


#获取存储费标准
def get_storage_fee_st(warehouse_id,mounth):
    sql='select * from cost_storage_plt where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    return mysql.get_all(sql)

#获取订单操作工时费标准
def get_operation_st(warehouse_id,mounth):
    sql='select * from cost_order_operation where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)
#获取耗材使用标准
def get_material_st(warehouse_id,mounth):
    sql='select * from cost_material_stand where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)
#获取耗材单价标准
def get_material_price_st(warehouse_id,mounth):
    sql='select * from cost_material_price where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)

#获取各仓工时计费标准
def get_category_operation_st(warehouse_id,mounth):
    sql='select * from cost_category_operation where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)


mysqlonline=MySQL('localhost','root','zt1234567','costanalysis')


#获取客户存储托盘数量
def get_storage_pallet(cus):
    sql='select * from cost_storage_plt where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    return mysql.get_all(sql)

#获取客户订单操作量
def get_storge_outstock(warehouse_id,mounth):
    sql='select * from cost_order_operation where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)
#获取客户增值服务数据
def get_storge_add(warehouse_id,mounth):
    sql='select * from cost_material_stand where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)
#获取耗材使用数据
def get_storge_material(warehouse_id,mounth):
    sql='select * from cost_material_price where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)

#获取客户配送数据
def get_dispatch(warehouse_id,mounth):
    sql='select * from cost_category_operation where warehouse_id="{}" and month={}'.format(warehouse_id,mounth)
    print(sql)
    return mysql.get_all(sql)







#print(get_storage_fee_st('123',5))
#print(get_operation_st('123',5))
#print(get_material_st('123',5))
#print(get_material_price_st('123',5))
#print(get_category_operation_st('123',5))

