from operator import index

import pandas as pd
import numpy as np
from pandas import DataFrame, Series, date_range

# a = pd.Series([5,6,7,8])
# b = pd.Series([5,6,7,8], index = ['a','b','c', 'd'])
# c = pd.date_range('01.01.2010','10.01.2010')
# e = pd.date_range('2010-04-01','2010-04-06')

dates = pd.date_range('2010-01-01','2010-01-05')

temps1 = pd.Series([80,82,85,90,83], index = dates )
temps2 = pd.Series([78,175,69,79,77], index = dates  )

diff_temp = temps1 - temps2
# print(temps1 - temps2)

temp_ds = pd.DataFrame(
    {'Msk': temps1,
     'Spb': temps2}
)
cols = ['Msk','Spb']
# print(temp_ds)
temp_ds['Diff'] = temp_ds.Msk - temp_ds.Spb
# print(temp_ds.iloc[[1,3]])
print(temp_ds)
print(temp_ds[temp_ds.Msk > 83])
# print()
# print(type(temp_ds.loc['2010-01-04']))
# print(temp_ds.loc['2010-01-04'].iloc[1])