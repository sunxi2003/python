from pyecharts.charts import Pie #饼图所导入的包
from pyecharts import options as opts #全局设置所导入的包

v1 = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v2 = [11, 12, 13, 10, 10, 10]
my_chart = Pie()
my_chart.add("",[list(z) for z in zip(v1,v2)])
my_chart.set_global_opts(title_opts=opts.TitleOpts("品类销售占比"))
my_chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
my_chart.render('pie.html')



