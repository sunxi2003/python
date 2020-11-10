# pivot: 数据透视（行转列）
import pandas as pd

#读取数据
data = pd.read_excel('./the_pandas/pallet.xlsx')
print(len(data))

#方法1: pivot(‘index=xx’,’columns=xx’,’values=xx’)   
print(data.pivot(index='name', columns='month', values='qty'))

#方法2: pivot(‘索引列’，‘列名’，‘值’)
print(data.pivot('name', 'month', 'qty'))