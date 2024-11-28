
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ind0 = ['a','b','c','d','e']
ind = ['col1', 'col2', 'col3', 'col4']
# temp_msk = [20,15]
temp_msk = pd.Series(np.arange(5,25,2))
# print(temp_msk)
# temp_msk = [20,15]
# temp_spb = [16,18]
temp_spb = pd.Series(np.arange(50,60))


t = {'msk':temp_msk,
     'spb':temp_spb
     }
# df1 = pd.DataFrame([temp_msk, temp_spb], columns=['temp_msk', 'temp_spb'])
df1 = pd.DataFrame(t)


df2 = df1[:3].copy()
df2['spb'] = df2['spb'] + 100

# print(df1)
# pd.concat([df1,df2],axis=1)
df2['Test'] = 3
df3 = pd.concat([df1, df2],ignore_index=False, keys=['l1','l2'])
print(df3.msk)
df3.loc(len(af3))
d3


sp500 = pd.read_csv(r'c:\ML\LearningPandas\Data\sp500.csv',index_col=['Symbol'], usecols=[0,2,3,7])
# sp500['Name'] = sp500['Name'].str.lower()
# print(sp500.at['ABBV','Price'])
# print(sp500.Price['ABBV'])
# print(sp500.iat[2,1])
# data.columns = map(str.lower, data.columns)
# or
# data.columns = [x.lower() for x in data.columns]

# print(len(df))
# s[4] = 'col4'
# print(s)
# print(s.index)
# # s.concat
# print(s)

# x = pd.Series()
# N = 4
# for i in range(N):
#    x = x.set_value(i, i**2)
# print(x)
