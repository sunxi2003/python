import pandas as pd

data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
        'year': [2016, 2016, 2015, 2017, 2016, 2016],
        'population': [2100, 2300, 1000, 700, 500, 500]}
df = pd.DataFrame(data, columns=['year', 'city', 'population', 'debt'])

condition = ['Beijing', 'Shanghai']

# in
print("———————————— in ————————————")
print(df.loc[df['city'].isin(condition)])

# not in
print("———————————— not in ————————————")
print(df.loc[~df['city'].isin(condition)])
