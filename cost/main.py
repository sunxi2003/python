from sqlalchemy import create_engine
import cost.do_storage_cost as storage
import cost.do_operation_cost as operation
import cost.do_material_cost as material
import cost.do_add_cost as add
import cost.do_dispatch as dispatch

# 服务器BMS
bms=create_engine('mysql+pymysql://bms_prd_zt_ls:bms_prd_zt-test@345@172.20.22.44:3306/bmssite_prd')

# 月份
month = '202006';
# 商家
customer_id = '1100002212';
customer_name = '联合利华'

# 1100001514：福建圣农
# 1100002325: 湾仔码头(通用磨坊)
# 1100002212：联合利华（北京一商）

# 匹配宅配成本
# dispatch.do_cost(bms,month,customer_id,customer_name) ;

# 计算存储费成本
# storage.do_cost(bms,month,customer_id,customer_name) ;

# 计算订单操作费成本
# operation.do_cost(bms,month,customer_id,customer_name);

# 计算耗材成本
material.do_cost(bms,month,customer_id,customer_name);

# # 计算增值服务成本
# add.do_cost(bms,month,customer_id,customer_name);




