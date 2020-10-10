from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts

line = Line()

# 设置数据
# 添加x轴，Faker.choose(): 使用faker的随机数据生成x轴标签
line.add_xaxis(Faker.provinces)
# 添加y轴，Faker.values(): 使用faker的随机数据生成y轴数值
line.add_yaxis('数据1',Faker.values())
line.set_global_opts(title_opts=opts.TitleOpts(title='Line 基本示例'))

line.render("line.html")